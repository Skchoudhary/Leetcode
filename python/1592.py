class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        total_spaces = text.count(' ')
        word_count =  [d for d in text.split(' ') if d != '']
        if len(word_count) < 2:
            n_text = text.strip() + (' ' * total_spaces)
            return n_text
        max_space = total_spaces / (len(word_count) - 1)
        
        d = ' ' * int(max_space)
        n_text = d.join(word_count)    
        n_text = n_text.strip(' ')
        left_over_space = total_spaces -  (int(max_space) * (len(word_count) -1))
        n_text += ' ' * left_over_space
        return n_text
