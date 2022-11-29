### Test code to make .csv more pretty

```
filename = 'testDataNov292022_V15'
fullAddress = os.path.join(data_dir, filename)                                  #instead of typing a file name in the 'with open', this creates a filename and the place to save it

with open(fullAddress + '.csv', mode='w', newline='') as csvFile:
    fieldnames = ['block', 'trial', 'problem','correct_answer','subject_response','subject_accuracy', 'response_time'] 
    data_writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    
    data_writer.writeheader()
    for iTrial in range(nTrials):
        data_writer.writerow({'block':iTrial,                               
                              'trial':1,
                              'problem':prob[iTrial][0],
                              'correct_answer':corr_resp[iTrial][0],
                              'subject_response':sub_resp[iTrial][0],
                              'subject_accuracy':sub_acc[iTrial][0],
                              'response_time':resp_time[iTrial][0]})
        data_writer.writerow({'block':iTrial,
                              'trial':2,
                              'problem':prob[iTrial][1],
                              'correct_answer':corr_resp[iTrial][1],
                              'subject_response':sub_resp[iTrial][1],
                              'subject_accuracy':sub_acc[iTrial][1],
                              'response_time':resp_time[iTrial][1]})
        data_writer.writerow({'block':iTrial,
                              'trial':3,
                              'problem':prob[iTrial][2],
                              'correct_answer':corr_resp[iTrial][2],
                              'subject_response':sub_resp[iTrial][2],
                              'subject_accuracy':sub_acc[iTrial][2],
                              'response_time':resp_time[iTrial][2]})
```
NOTE: Works, but kinda clunnky. I can't figure out how to get the 'trial' to input correctly without hand-typing the number. The iTrial in this loop actually loops more like an 'for iBlock in range(nTrials)'. 


```
filename = 'testDataNov292022'
fullAddress = os.path.join(data_dir, filename)                                  #instead of typing a file name in the 'with open', this creates a filename and the place to save it

with open(fullAddress + '.csv', mode='w', newline='') as csvFile:
    fieldnames = ['block', 'trial', 'problem','correct_answer','subject_response','subject_accuracy', 'response_time']
    data_writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    
    data_writer.writeheader()
    for iBlock in range(nBlocks):
        for iTrial in range(nTrials):
            data_writer.writerow({'block':iBlock, 'trial':iTrial,
                                  'problem':prob[iBlock]['problem'][iTrial],
                                  'correct_answer':corr_resp[iBlock]['correct_answer'][iTrial],
                                  'subject_response': sub_resp[iBlock]['subject_response'][iTrial],
                                  'subject_accuracy': sub_acc[iBlock]['subject_accuracy'][iTrial],
                                  'response_time': resp_time[iBlock]['response_time'][iTrial]})
```
NOTE: There is a TypeError in this image (I think it has something to with using the fieldname in the second index??). I threw in some code to see the dict_values and dict_keys to try to use these as the integer the TypeError is asking for, but now I am lost.
