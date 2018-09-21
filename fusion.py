import numpy as np
import pdb

files_scores = ['./output/flow_score.npz','./output/TRUE.npz']

'''
def compute_acc(labels, scores):

    #pdb.set_trace()
    preds_max = np.argmax(scores)
    num_correct = np.sum(preds == labels)
    acc = num_correct * 1.0 / preds.shape[0]
    return acc

for filename in files_scores:
    data = np.load(filename)
    preds = data['predictions']
    labels = data['labels']
    scores = data['scores']
    acc_scores = compute_acc(labels, scores)
    num_correct = np.sum(preds == labels)
    acc = num_correct * 1.0 / preds.shape[0]
    print('acc=%.3f acc_score=%.3f %s' % (acc, acc_scores, filename))
   '''

data1 = np.load(files_scores[0])
preds1 = data1['predictions']
labels1 = data1['labels']
scores1 = data1['scores']

data2 = np.load(files_scores[1])
preds2 = data2['predictions']
labels2 = data2['labels']
scores2 = data2['scores']


scores4 = scores1 * 1.43 + scores2 #rgb 3 flow 1
scores3 = scores1 + scores2

pred_max =  []
pred_max5 = []

for i in range(10000):
    tmp = scores3[i]
    pred_max.append(np.argmax(tmp[0]))
    c = np.argpartition(tmp[0][0][0],-5)[-5:]
    pred_max5.append(c)


print(pred_max)
print(str(len(pred_max)))
print("max5: " + str(len(pred_max5)))

num_correct = np.sum(pred_max == labels1)

k = []
for i in range(10000):
    k.append(  np.isin(pred_max5[i],labels1[i]) )

num_correct5 = np.sum(k)

print('r:f=1:1 top1 result : ' + str(num_correct) )
print('r:f=1:1 top5 result : '+ str(num_correct5))

#

pred_max = []
pred_max5 = []

for i in range(10000):
    tmp = scores4[i]
    pred_max.append(np.argmax(tmp[0]))
    c = np.argpartition(tmp[0][0][0], -5)[-5:]
    pred_max5.append(c)

print(pred_max)
print(str(len(pred_max)))
print("max5: " + str(len(pred_max5)))


num_correct = np.sum(pred_max == labels1)

k = []
for i in range(10000):
    k.append(  np.isin(pred_max5[i],labels1[i]) )

num_correct5 = np.sum(k)

print('r:f=1:1.43 top1 result : ' + str(num_correct))
print('r:f=1:1.43 top5 result : ' + str(num_correct5))