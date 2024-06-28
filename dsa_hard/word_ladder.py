import math

def is_valid(cur_word, cand_word):
    if set(cur_word) - set(cand_word) != 1:
        return False
    else:
        return True

def word_ladder(solution, current_word, end_word, array):
    if current_word == end_word:
        return len(solution)

    else:
        min_cand_score = math.inf
        for word in array:
            # validation
            if word not in solution and is_valid(current_word, word):
                cand_score = word_ladder(solution.add(word), word, end_word, array)
                
                if cand_score < min_cand_score:
                    min_cand_score = cand_score

        return min_cand_score

first_word = "hit"
end_word = "cog"
word_list = set(["hot", "dot", "dog", "lot", "log"])
print(word_ladder(set(), first_word, end_word, word_list))
