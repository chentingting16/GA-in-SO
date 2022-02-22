# GA Replication package

Our reproducibility package (data and scripts) for GA study (Our [MSR'22](https://conf.researchr.org/home/msr-2022) paper). 

## Quantitative study
### Data
#### Posts(the SO posts about GA)
- posts.xlsx
(Id,title,content,URL)
#### Posts with categories
- posts_category.xlsx
(Id,title,content,URL,Description,Cate,answerCount,hasAcceptedAnswer,acceptedAnswerId,qCreationDate,aLastEditDate,responseTime)
#### Expertise
- expert.xls
(type,AVG(ViewCount),AVG(FavoriteCount),AVG(AnswerCount),AVG(ANSSCORE),AVG(ownerreputation),AVG(ownerviewcount))
#### Kendall
- kendall.csv
(Category,mean_view,mean_favorite,mean_score,%acc_ans,%wo_acc,resp_time(min))
- kendall.xlsx
(co-efficient/p-value,AvgView,AvgFav,AvgScore)
#### Summary(difficulty, popularity...)
- summary.xlsx


### Models and Scripts
- Post Collection: data.py
- Data Preprocess: data_preprocess.py
- Expert Comparison: expert_comparison_all.py


