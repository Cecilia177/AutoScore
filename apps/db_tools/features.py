
from db_tools.sentence import Sentence
from db_tools.LSA import LSA
from db_tools.vecsim import get_min_WCD
from db_tools.partofspeech import get_phrases_ratio
from db_tools.dictionany import get_key_match
from db_tools.fluency import get_fluency_score


def cal_features(refs, answers, answer_ids, question_type, word2vec_model, nlp_model):
    """
    Calculate features of texts of all courses and questions and insert those into DB.
    To put it simple, complete the features table in DB.
    Parameters:
        conn: A mysql connection.

    """
    language = "ch" if question_type == 3 else "en"

    # Build docs matrix for every question.
    ref_num, textids, doc_matrix = get_docs_list(refs, answers, answer_ids, question_type)
    mylsa = build_svd(doc_matrix)
    references = doc_matrix[: ref_num]  # terms in references are Class Sentence and are preprocessed already.
    original = Sentence(text="", language='en')
    original.preprocess()
    features_list = {}

    for i in range(ref_num, len(doc_matrix)):
        features = []
        current_answer = doc_matrix[i]

        # Calculate features including LENGTHRATIO, 1~4GRAM, LSAGRADE, VEC_SIM, etc.
        lengthratio = get_lengthratio(refs=references, answer=current_answer)
        ngrams = get_bleu_score(refs=references, answer=current_answer)
        lsagrade = mylsa.get_max_similarity(10, i, ref_num)
        vec_sim = get_min_WCD(id=i, vecs=word2vec_model, stopwords=[], tf_idf=mylsa.A,
                              keys=mylsa.keys, ref_num=ref_num, language=language)
        fluency = get_fluency_score(refs=references, sentence=current_answer)
        np_length_ratio = get_phrases_ratio(phrase="NP", refs=references, answer=current_answer, model=nlp_model)
        vp_length_ratio = get_phrases_ratio(phrase="VP", refs=references, answer=current_answer, model=nlp_model)
        keymatch = get_key_match(original=original, trans=current_answer, vecs=word2vec_model) if question_type == 3 else None
        features.append(ngrams[0])
        features.append(ngrams[1])
        features.append(ngrams[2])
        features.append(ngrams[3])
        features.append(lengthratio)
        features.append(lsagrade)
        features.append(vec_sim)
        features.append(fluency)
        features.append(np_length_ratio)
        features.append(vp_length_ratio)
        if question_type == 3:
            features.append(keymatch)

        textid = textids[i]
        features_list[textid] = features
    return features_list


def build_svd(docs_list):
    """
    Parameters:
        A list of docs.
    Returns:
        A LSA object, containing matrix A as tf-idf matrix,
            and method get_similarity() to cal the similarity between 2 docs in docs_list.
    """
    # build count matrix, tf-idf modification matrix and get svd.
    lsa = LSA(stopwords=[], ignorechars="")
    for doc in docs_list:
        lsa.parse(doc)
    lsa.build_count_matrix()
    lsa.TFIDF()
    lsa.svd_cal()
    return lsa


def get_docs_list(refs, answers, answer_ids, question_type):
    """
    Assemble references and answers of the same question to a doc matrix.

    Parameters:
        refs: List of references text.
        answers: List of answers text.
        answer_ids: List of answer ids, with the same order of answers list
        question_type: 3 or 4, refs and answers text is Chinese if 3 or else English
    Return:
        Integer: number of references
        textids: list of textid and list of doc(class Sentence), the first terms of both are negative.
        doc_matrix: List of references and answers of the same question, items of which are Sentence class and
        preprocessed already.
    """

    lang = "ch" if question_type == 3 else "en"
    doc_matrix = []
    textids = []
    ref_id = -1
    for ref in refs:
        reference = Sentence(text=ref, language=lang)
        reference.preprocess()
        doc_matrix.append(reference)   # add Sentence references as the leading terms of doc_matrix
        textids.append(ref_id)   # Use negative numbers as reference id.
        ref_id -= 1

    for dt in answers:
        cur_ans = Sentence(text=dt, language=lang)
        cur_ans.preprocess()
        doc_matrix.append(cur_ans)
    textids.extend(answer_ids)
    return len(refs), textids, doc_matrix


def get_lengthratio(refs, answer):
    """
    Parameters:
        refs: List, item of which is class Sentence
        answer: class Sentence
    Return:
        float, answer length / average ref length
    """
    ref_length = 0
    for ref in refs:
        ref_length += ref.seg_length
    length = float(ref_length) / len(refs)
    return answer.seg_length / length


def get_bleu_score(refs, answer):
    """
    paras:
        refs: List, item of which is class Sentence
        answer: class Sentence
    Return:
        A list including maximum 1~4gram matching rate of answer compared to all the refs,
            e.g. [1gram rate, 2gram rate, 3gram rate, 4gram rate]
    """
    score_list = [0] * 4
    if answer.seg_length == 0:
        return score_list
    for ref in refs:
        ref_ngram = ref.ngram
        answer_ngram = answer.ngram
        total_count = [0] * 4
        match_count = [0] * 4
        for key in answer_ngram.keys():
            n = len(key.split(" ")) - 1   # key is (n+1)gram
            total_count[n] += answer_ngram[key]
            if key in ref_ngram.keys():
                match_count[n] += min(answer_ngram[key], ref_ngram[key])
        for i in range(4):
            score_list[i] = max(float(score_list[i]), float(match_count[i]) / total_count[i])
    return score_list





