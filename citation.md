## Context
now, i am writing a blog, and i am finalizing it by adding reference. 

I have collected a series of Bibex citation, and i need you help me transform them into HTML form


For example
---

### bib form
@misc{black2024pi0visionlanguageactionflowmodel,
      title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control}, 
      author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},
      year={2024},
      eprint={2410.24164},
      archivePrefix={arXiv},
      primaryClass={cs.LG},


### html form
            <div class="csl-entry">
            K. Black, N. Brown, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, L. Groom, K. Hausman, B. Ichter, et al. (2024).

              Black, o., Xia, Z., Ha, L., Kaplan, A., Huang, H., Hausman, K., Ichter, B., Fox, D., & Levine, S. (2024). 
              <span class="paper-title">π0: A vision-language-action flow model for general robot control.</span>
              <span class="paper-conference">arXiv preprint arXiv:2410.24164.</span>
              <a href="https://arxiv.org/abs/2410.24164">[Paper]</a>
              <a href="https://www.pi.website/blog/pi0">[Project Page]</a>
            </div>

---

Now, i need you help me turn below into HTML form list. 
The source paper & website will be a mix of bib and more casual format, i just need HTML version. 

---

K. Pertsch, K. Stachowicz, B. Ichter, D. Driess, S. Nair, Q. Vuong, O. Mees, C. Finn, and
S. Levine. Fast: Efficient action tokenization for vision-language-action models. arXiv preprint
arXiv:2501.09747, 2025.
https://www.pi.website/research/fast


@inproceedings{10.5555/3692070.3692401,
author = {Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios N. and Li, Tianle and Li, Dacheng and Zhu, Banghua and Zhang, Hao and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},
title = {Chatbot arena: an open platform for evaluating LLMs by human preference},
year = {2024},
publisher = {JMLR.org},
abstract = {Large Language Models (LLMs) have unlocked new capabilities and applications; however, evaluating the alignment with human preferences still poses significant challenges. To address this issue, we introduce Chatbot Arena, an open platform for evaluating LLMs based on human preferences. Our methodology employs a pairwise comparison approach and leverages input from a diverse user base through crowdsourcing. The platform has been operational for several months, amassing over 240K votes. This paper describes the platform, analyzes the data we have collected so far, and explains the tried-and-true statistical methods we are using for efficient and accurate evaluation and ranking of models. We confirm that the crowdsourced questions are sufficiently diverse and discriminating and that the crowd-sourced human votes are in good agreement with those of expert raters. These analyses collectively establish a robust foundation for the credibility of Chatbot Arena. Because of its unique value and openness, Chatbot Arena has emerged as one of the most referenced LLM leaderboards, widely cited by leading LLM developers and companies. The platform is publicly available at https://chat.lmsys.org.},
booktitle = {Proceedings of the 41st International Conference on Machine Learning},
articleno = {331},
numpages = {30},
location = {Vienna, Austria},
series = {ICML'24}
}


 



 Piyush Sharma, Nan Ding, Sebastian Goodman, and Radu Soricut. 2018. Conceptual Captions: A Cleaned, Hypernymed, Image Alt-text Dataset For Automatic Image Captioning. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 2556–2565, Melbourne, Australia. Association for Computational Linguistics.


 Soravit Changpinyo, Doron Kukliansy, Idan Szpektor, Xi Chen, Nan Ding, and Radu Soricut. 2022. All You May Need for VQA are Image Captions. In Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 1947–1963, Seattle, United States. Association for Computational Linguistics.


@article{OpenImages,
  author = {Alina Kuznetsova and Hassan Rom and Neil Alldrin and Jasper Uijlings and Ivan Krasin and Jordi Pont-Tuset and Shahab Kamali and Stefan Popov and Matteo Malloci and Alexander Kolesnikov and Tom Duerig and Vittorio Ferrari},
  title = {The Open Images Dataset V4: Unified image classification, object detection, and visual relationship detection at scale},
  year = {2020},
  journal = {IJCV}
}




---


Notice, when you are adding html citation, you should keep italic, link correctly

