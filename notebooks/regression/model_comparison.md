## Значения RMSE

### DeepPavlov_ruberta_base_cased

* EPOCHS = 10
* SEED = 2021
* MAX_LENGTH = 200
* BATCH_SIZE = 8

scheduler = StepLR(optimizer, step_size=30, gamma=0.1)


| Таргет                  | Test           |
|-------------------------|----------------|
| disgust_rage            | 2.206          |
| enjoyment_distress      | 2.611          |
| fear_surprise           | 2.303          |
| shame_excitement        | 2.376          |


### iss_bert_base_multilingual_cased

* EPOCHS = 5
* SEED = 2021
* MAX_LENGTH = 200
* BATCH_SIZE = 8


| Таргет                  | Test           |
|-------------------------|----------------|
| disgust_rage            | 2.251          |



### iss_bert_base_multilingual_cased + StepLR

* EPOCHS = 5
* SEED = 2021
* MAX_LENGTH = 200
* BATCH_SIZE = 8

scheduler = StepLR(optimizer, step_size=30, gamma=0.1)

| Таргет                  | Test           |
|-------------------------|----------------|
| disgust_rage            | 2.262          |



