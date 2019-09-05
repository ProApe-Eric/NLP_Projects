# BLUE Score Implementation
1. The notebook includes all details about the functions
2. BLEU.py is the cleaned version as package for other jobs

###Functions in *BLEU.py*
1. Simple Bleu Score for ngram  
   ```python
   def bleu_ngram(ref_list, mt_out, ngram, toLowerCase=True, stripPunctuation=False)
   ```
2. Combines Bleu Score with brevity penalty choice
   ```python
   def combined_exp_bleu_ngram(ref_list, mt_out, ngram, bp=True ,toLowerCase=True, stripPunctuation=False)
   ```