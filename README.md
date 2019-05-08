# MIR_HW1

## Q1 (GTZAN)
1. Q1: 以“*GTZAN*”為Dataset, 作基本template 上的預測

Q1結果：
```gherkin=
GTZAN
***** Q1 *****
----------
Genre    	accuracy
pop      	    41%
metal    	    25%
disco    	    32%
blues    	    7%
reggae   	    33%
classical	    -
rock     	    35%
hiphop   	    14%
country  	    32%
jazz     	    16%
----------
Overall accuracy:	27%
```
高分者：
pop和rock類的表現較佳，可能是因為在這兩個音樂類型上，較常使用一般的七聲音階及大小調的樂理技巧在作曲。

低分者：
blues和hiphop在作曲的編成上就不太一樣，而是使用特定的[Hexatonic](https://en.wikipedia.org/wiki/Hexatonic_scale) 及 [Heptatonic](https://en.wikipedia.org/wiki/Heptatonic_scale)

## Q1-2 (GiantSteps)
2. Q1-2: 以“*GiantSteps*”為Dataset, 作基本template 上的預測

Q1-2結果：
```gherkin=
GiantSteps
***** Q1-2 *****
----------
Overall accuracy:	22%
```
如上結果

## Q2
3. Q2: 
以“*GTZAN*”為Dataset, 加入**gamma**的變動參數作nonlinear transform上的預測

Q2結果：
```gherkin=
GTZAN
***** Q2 *****
----------
'gamma = 1'

Genre    	accuracy
pop      	    40%
metal    	    22%
disco    	    33%
blues    	    7%
reggae   	    32%
classical	    -
rock     	    34%
hiphop   	    14%
country  	    34%
jazz     	    16%

Overall accuracy:	26%
----------
'gamma = 10'

Genre    	accuracy
pop      	    39%
metal    	    19%
disco    	    29%
blues    	    4%
reggae   	    29%
classical	    -
rock     	    31%
hiphop   	    15%
country  	    31%
jazz     	    11%

Overall accuracy:	24%
----------
'gamma = 100'

Genre    	accuracy
pop      	    34%
metal    	    19%
disco    	    29%
blues    	    4%
reggae   	    25%
classical	    -
rock     	    28%
hiphop   	    10%
country  	    31%
jazz     	    14%

Overall accuracy:	22%
----------
'gamma = 1000'

Genre    	accuracy
pop      	    33%
metal    	    19%
disco    	    28%
blues    	    5%
reggae   	    26%
classical	    -
rock     	    29%
hiphop   	    9%
country  	    31%
jazz     	    14%

Overall accuracy:	22%
----------
```
gamma的參數添加，做了非線性的校正。
這邊看來是gamma = 1時，準確率較佳。
然而，參數的大小除了必須藉由實驗的不斷調整外，還需要根據樂曲型態而定，如：表現較差的blues在參數提高的情況有些微幅度回升。

## Q3
4. Q3: 
以“*GTZAN*”為Dataset, 利用**mir_eval.key**更改原先accuracy的計算

Q3結果：
```gherkin=
GTZAN
***** Q3 *****
Genre    	accuracy
pop      	    57%
metal    	    35%
disco    	    49%
blues    	    20%
reggae   	    48%
classical	    -
rock     	    49%
hiphop   	    20%
country  	    55%
jazz     	    32%
----------
Overall accuracy:	41%
```
這邊結果相較原先基本的template方法有明顯提升。
而提升的原因其實也很直覺，因為透過關係大小調、同名大小調的「權重」上考量，避免了**錯者全錯**的計算，將得以有效提升準確率。

## Q4 (GTZAN)
5. Q4:
以“*GTZAN*”為Dataset, 將基本template變成Krumhansl-Schmuckler’s method作預測

Q4結果：
```gherkin=
GTZAN
***** Q4 *****
Genre    	accuracy
pop      	    43%
metal    	    27%
disco    	    30%
blues    	    17%
reggae   	    36%
classical	    -
rock     	    35%
hiphop   	    15%
country  	    29%
jazz     	    16%
----------
Overall accuracy:	28%
```
KS template比較能呈現大小調音符的分佈關係，然而同Q1是透過correct的計算方式運算，可能會減少了許多可能正確的答案，因此準確率並未顯著提升。

## Q4-2 (GiantSteps)
6. Q4-2: 
以“*GiantSteps*”為Dataset, 將基本template變成Krumhansl-Schmuckler’s method作預測

Q4-2結果：
```gherkin=
GiantSteps
***** Q4-2 *****
----------
Overall accuracy:	28%
```
如上結果

## Q4_2 
7. Q4_2:
以“*GTZAN*”為Dataset, 加入**gamma**的變動參數作nonlinear transform上的預測

Q4_2結果：
```gherkin=
GTZAN
***** Q4_2 *****
----------
'gamma = 1'

Genre    	accuracy
pop      	    43%
metal    	    26%
disco    	    32%
blues    	    17%
reggae   	    35%
classical	    -
rock     	    34%
hiphop   	    12%
country  	    31%
jazz     	    15%

Overall accuracy:	28%
----------
'gamma = 10'

Genre    	accuracy
pop      	    40%
metal    	    25%
disco    	    27%
blues    	    17%
reggae   	    31%
classical	    -
rock     	    33%
hiphop   	    15%
country  	    28%
jazz     	    14%

Overall accuracy:	26%
----------
'gamma = 100'

Genre    	accuracy
pop      	    37%
metal    	    25%
disco    	    27%
blues    	    20%
reggae   	    28%
classical	    -
rock     	    32%
hiphop   	    12%
country  	    28%
jazz     	    15%

Overall accuracy:	25%
----------
'gamma = 1000'

Genre    	accuracy
pop      	    37%
metal    	    25%
disco    	    26%
blues    	    21%
reggae   	    30%
classical	    -
rock     	    32%
hiphop   	    11%
country  	    29%
jazz     	    15%

Overall accuracy:	26%
----------
```
這邊的gamma隨著1, 10, 100, 1000的參數設定有一些變動起伏，更印證實驗的參數拿捏的重要性，也是gamma作為非線性校正上的重要意涵。

## Q4_3
8. Q4_3:
以“*GTZAN*”為Dataset, 利用**mir_eval.key**更改原先accuracy的計算

Q4_3結果：
```gherkin=
GTZAN
***** Q4_3 *****
Genre    	accuracy
pop      	    57%
metal    	    39%
disco    	    46%
blues    	    30%
reggae   	    51%
classical	    -
rock     	    48%
hiphop   	    22%
country  	    52%
jazz     	    33%
----------
Overall accuracy:	43%
```
透過mir_eval並配合ks template是目前運算結果後的最佳解，同時也證明好的運算也必需要配合好的評估標準，才能使結果達到最好的預期。

## Q5
9. Q5:
以“*BPS-FH*”為Dataset, 實作local key detection的預測
