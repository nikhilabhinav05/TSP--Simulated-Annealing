Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> x1_file = pd.ExcelFile('C:/Users/nabhinav/AppData/Local/Programs/Python/Python36/IGA.xlsx')
>>> 
>>> items=x1_file.parse('Sheet1')
>>> items.head()
     ItemGroupId       I1         I2         I3 ...   I31  I32  I33  I34
0  1_13069000301  2274736        NaN        NaN ...   NaN  NaN  NaN  NaN
1  1_13069000502  2556261  2556259.0  2556257.0 ...   NaN  NaN  NaN  NaN
2  1_13069000701  2458678  2274748.0        NaN ...   NaN  NaN  NaN  NaN
3  1_13069060001  2274773        NaN        NaN ...   NaN  NaN  NaN  NaN
4  1_13602713301  2366859  2274795.0        NaN ...   NaN  NaN  NaN  NaN

[5 rows x 35 columns]
>>> items.head(n=100)
      ItemGroupId       I1         I2         I3 ...         I31  I32  I33  I34
0   1_13069000301  2274736        NaN        NaN ...         NaN  NaN  NaN  NaN
1   1_13069000502  2556261  2556259.0  2556257.0 ...         NaN  NaN  NaN  NaN
2   1_13069000701  2458678  2274748.0        NaN ...         NaN  NaN  NaN  NaN
3   1_13069060001  2274773        NaN        NaN ...         NaN  NaN  NaN  NaN
4   1_13602713301  2366859  2274795.0        NaN ...         NaN  NaN  NaN  NaN
5   1_15326560001  2479975        NaN        NaN ...         NaN  NaN  NaN  NaN
6   1_30235000101  2274876  2274878.0  2274877.0 ...         NaN  NaN  NaN  NaN
7   1_30796060201  2617789  2617788.0  2617787.0 ...         NaN  NaN  NaN  NaN
8   1_30831700301  2275443  2275445.0  2275437.0 ...         NaN  NaN  NaN  NaN
9   1_30849911701  2275607  2275604.0  2275610.0 ...         NaN  NaN  NaN  NaN
10  1_31081110001  2275906  2348465.0  2275908.0 ...         NaN  NaN  NaN  NaN
11  1_31242200301  2479982  2479983.0  2479984.0 ...         NaN  NaN  NaN  NaN
12  1_31242200601  2512435  2512431.0  2512430.0 ...         NaN  NaN  NaN  NaN
13  1_31249813401  2368523        NaN        NaN ...         NaN  NaN  NaN  NaN
14  1_31283400401  2539179  2481204.0  2493149.0 ...         NaN  NaN  NaN  NaN
15  1_31741501301  2721989        NaN        NaN ...         NaN  NaN  NaN  NaN
16  1_31775403901  2643764  2643759.0  2643765.0 ...         NaN  NaN  NaN  NaN
17  1_31842903201  2276763  2276752.0  2276764.0 ...         NaN  NaN  NaN  NaN
18  1_31842904101  2361482        NaN        NaN ...         NaN  NaN  NaN  NaN
19  1_31842930501  2276935  2276934.0  2276936.0 ...         NaN  NaN  NaN  NaN
20  1_32521320501  2720062  2724163.0  2724164.0 ...         NaN  NaN  NaN  NaN
21  1_32521350701  2277194  2277193.0        NaN ...         NaN  NaN  NaN  NaN
22  1_33214802401  2469337        NaN        NaN ...         NaN  NaN  NaN  NaN
23  1_33214810601  2277326  2277329.0  2277328.0 ...         NaN  NaN  NaN  NaN
24  1_33214811601  2469338        NaN        NaN ...         NaN  NaN  NaN  NaN
25  1_33214860801  2277359  2277358.0  2277361.0 ...         NaN  NaN  NaN  NaN
26  1_33255080001  2277582  2277571.0  2277573.0 ...         NaN  NaN  NaN  NaN
27  1_35515210601  2277854        NaN        NaN ...         NaN  NaN  NaN  NaN
28  1_36088400101  2416984  2416983.0  2416982.0 ...         NaN  NaN  NaN  NaN
29  1_37781212301  2721993        NaN        NaN ...         NaN  NaN  NaN  NaN
..            ...      ...        ...        ... ...         ...  ...  ...  ...
70  1_70547513001  2460272        NaN        NaN ...         NaN  NaN  NaN  NaN
71  1_71815220601  2287231  2287232.0  2287240.0 ...         NaN  NaN  NaN  NaN
72  1_72401001501  2287481  2287480.0  2287478.0 ...         NaN  NaN  NaN  NaN
73  1_72487701201  2460278        NaN        NaN ...         NaN  NaN  NaN  NaN
74  1_74968000501  2693849  2693851.0  2693846.0 ...         NaN  NaN  NaN  NaN
75  1_74968840501  2693854  2693853.0  2693855.0 ...         NaN  NaN  NaN  NaN
76  1_74976601401  2289556        NaN        NaN ...         NaN  NaN  NaN  NaN
77  1_74976603101  2718030  2718032.0  2718031.0 ...         NaN  NaN  NaN  NaN
78  1_74977140001  2407154  2407152.0  2407162.0 ...         NaN  NaN  NaN  NaN
79  1_80754200201  2740544        NaN        NaN ...         NaN  NaN  NaN  NaN
80  1_81265441401  2293063  2293064.0  2293062.0 ...         NaN  NaN  NaN  NaN
81  1_81265500501  2682374        NaN        NaN ...         NaN  NaN  NaN  NaN
82  1_81265560601  2628703  2628704.0  2628706.0 ...         NaN  NaN  NaN  NaN
83  1_81801880201  2293882  2293889.0        NaN ...         NaN  NaN  NaN  NaN
84  1_81915130301  2294601  2294593.0        NaN ...         NaN  NaN  NaN  NaN
85  1_81919100401  2632536  2632549.0        NaN ...         NaN  NaN  NaN  NaN
86  1_81921300401  2740546  2362850.0  2740844.0 ...         NaN  NaN  NaN  NaN
87  1_81968501601  2686268  2686262.0  2686261.0 ...         NaN  NaN  NaN  NaN
88  1_81989900701  2298505        NaN        NaN ...         NaN  NaN  NaN  NaN
89  1_82351120101  2558970  2592518.0  2558972.0 ...         NaN  NaN  NaN  NaN
90  1_82633200801  2740548  2741928.0        NaN ...         NaN  NaN  NaN  NaN
91  1_82648841001  2719514  2719510.0  2719519.0 ...         NaN  NaN  NaN  NaN
92  1_82804160101  2300088  2300082.0  2300083.0 ...         NaN  NaN  NaN  NaN
93  1_82824601901  2740549        NaN        NaN ...         NaN  NaN  NaN  NaN
94  1_82840740501  2300572  2300573.0  2300571.0 ...         NaN  NaN  NaN  NaN
95  1_83194360101  2301166  2301165.0  2301167.0 ...         NaN  NaN  NaN  NaN
96  1_83194530301  2301248  2301246.0  2301250.0 ...         NaN  NaN  NaN  NaN
97  1_83194560101  2301281        NaN        NaN ...         NaN  NaN  NaN  NaN
98  1_83195800101  2723285  2723284.0  2723269.0 ...   2523634.0  NaN  NaN  NaN
99  1_83196180101  2385869  2385871.0  2385873.0 ...         NaN  NaN  NaN  NaN

[100 rows x 35 columns]
>>>  [100 rows x 35 columns]
SyntaxError: unexpected indent
>>> 
>>> import xlsxwriter
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    import xlsxwriter
ModuleNotFoundError: No module named 'xlsxwriter'
>>> 
>>> import xlsxwriter
>>> 
>>> 
>>> items
       ItemGroupId       I1         I2         I3 ...   I31  I32  I33  I34
0    1_13069000301  2274736        NaN        NaN ...   NaN  NaN  NaN  NaN
1    1_13069000502  2556261  2556259.0  2556257.0 ...   NaN  NaN  NaN  NaN
2    1_13069000701  2458678  2274748.0        NaN ...   NaN  NaN  NaN  NaN
3    1_13069060001  2274773        NaN        NaN ...   NaN  NaN  NaN  NaN
4    1_13602713301  2366859  2274795.0        NaN ...   NaN  NaN  NaN  NaN
5    1_15326560001  2479975        NaN        NaN ...   NaN  NaN  NaN  NaN
6    1_30235000101  2274876  2274878.0  2274877.0 ...   NaN  NaN  NaN  NaN
7    1_30796060201  2617789  2617788.0  2617787.0 ...   NaN  NaN  NaN  NaN
8    1_30831700301  2275443  2275445.0  2275437.0 ...   NaN  NaN  NaN  NaN
9    1_30849911701  2275607  2275604.0  2275610.0 ...   NaN  NaN  NaN  NaN
10   1_31081110001  2275906  2348465.0  2275908.0 ...   NaN  NaN  NaN  NaN
11   1_31242200301  2479982  2479983.0  2479984.0 ...   NaN  NaN  NaN  NaN
12   1_31242200601  2512435  2512431.0  2512430.0 ...   NaN  NaN  NaN  NaN
13   1_31249813401  2368523        NaN        NaN ...   NaN  NaN  NaN  NaN
14   1_31283400401  2539179  2481204.0  2493149.0 ...   NaN  NaN  NaN  NaN
15   1_31741501301  2721989        NaN        NaN ...   NaN  NaN  NaN  NaN
16   1_31775403901  2643764  2643759.0  2643765.0 ...   NaN  NaN  NaN  NaN
17   1_31842903201  2276763  2276752.0  2276764.0 ...   NaN  NaN  NaN  NaN
18   1_31842904101  2361482        NaN        NaN ...   NaN  NaN  NaN  NaN
19   1_31842930501  2276935  2276934.0  2276936.0 ...   NaN  NaN  NaN  NaN
20   1_32521320501  2720062  2724163.0  2724164.0 ...   NaN  NaN  NaN  NaN
21   1_32521350701  2277194  2277193.0        NaN ...   NaN  NaN  NaN  NaN
22   1_33214802401  2469337        NaN        NaN ...   NaN  NaN  NaN  NaN
23   1_33214810601  2277326  2277329.0  2277328.0 ...   NaN  NaN  NaN  NaN
24   1_33214811601  2469338        NaN        NaN ...   NaN  NaN  NaN  NaN
25   1_33214860801  2277359  2277358.0  2277361.0 ...   NaN  NaN  NaN  NaN
26   1_33255080001  2277582  2277571.0  2277573.0 ...   NaN  NaN  NaN  NaN
27   1_35515210601  2277854        NaN        NaN ...   NaN  NaN  NaN  NaN
28   1_36088400101  2416984  2416983.0  2416982.0 ...   NaN  NaN  NaN  NaN
29   1_37781212301  2721993        NaN        NaN ...   NaN  NaN  NaN  NaN
..             ...      ...        ...        ... ...   ...  ...  ...  ...
226  1_91777680101  2398962  2398963.0  2368213.0 ...   NaN  NaN  NaN  NaN
227  1_91779600201  2428134  2428135.0  2428137.0 ...   NaN  NaN  NaN  NaN
228  1_91820620001  2368280  2368284.0  2368286.0 ...   NaN  NaN  NaN  NaN
229  1_91820660001  2428156  2428153.0  2428155.0 ...   NaN  NaN  NaN  NaN
230  1_91820660101  2556720  2556721.0  2556722.0 ...   NaN  NaN  NaN  NaN
231  1_91820700301  2407744  2376189.0  2376192.0 ...   NaN  NaN  NaN  NaN
232  1_91823000301  2362553  2362551.0  2362563.0 ...   NaN  NaN  NaN  NaN
233  1_91823010001  2366676  2366668.0  2366669.0 ...   NaN  NaN  NaN  NaN
234  1_91826400301  2450328  2450327.0  2450322.0 ...   NaN  NaN  NaN  NaN
235  1_91835840001  2421999  2421995.0  2421990.0 ...   NaN  NaN  NaN  NaN
236  1_91971500201  2535866  2535863.0  2535867.0 ...   NaN  NaN  NaN  NaN
237  1_92149040701  2701504  2692249.0  2701502.0 ...   NaN  NaN  NaN  NaN
238  1_92149240001  2382198  2382199.0  2382196.0 ...   NaN  NaN  NaN  NaN
239  1_92151440701  2721271  2726639.0  2724337.0 ...   NaN  NaN  NaN  NaN
240  1_92206510401  2387078        NaN        NaN ...   NaN  NaN  NaN  NaN
241  1_92293340001  2347308  2347304.0  2347303.0 ...   NaN  NaN  NaN  NaN
242  1_92362000701  2347736  2347735.0  2347737.0 ...   NaN  NaN  NaN  NaN
243  1_94206000101  2357672  2357671.0  2407855.0 ...   NaN  NaN  NaN  NaN
244  1_94380640101  2735684  2735683.0  2735686.0 ...   NaN  NaN  NaN  NaN
245  1_AA051200201  2561585  2561583.0  2561586.0 ...   NaN  NaN  NaN  NaN
246  1_AA110900501  2566008  2566010.0  2566013.0 ...   NaN  NaN  NaN  NaN
247  1_AA134772501  2540613  2540614.0  2540612.0 ...   NaN  NaN  NaN  NaN
248  1_AA249410601  2726673  2722985.0  2722982.0 ...   NaN  NaN  NaN  NaN
249  1_AA396600301  2511116  2511111.0  2511113.0 ...   NaN  NaN  NaN  NaN
250  1_AA430201101  2552250  2552243.0  2552251.0 ...   NaN  NaN  NaN  NaN
251  1_AH678800101  2719910  2719909.0  2719912.0 ...   NaN  NaN  NaN  NaN
252  1_AJ202400101  2694263  2694249.0  2694259.0 ...   NaN  NaN  NaN  NaN
253  1_AJ516590101  2723086  2723087.0  2723089.0 ...   NaN  NaN  NaN  NaN
254  1_AJ731601001  2694522  2694521.0  2694524.0 ...   NaN  NaN  NaN  NaN
255  1_DUMMY0SKU01  2216783  2216784.0  2207483.0 ...   NaN  NaN  NaN  NaN

[256 rows x 35 columns]
>>> [256 rows x 35 columns]
SyntaxError: invalid syntax
>>> 
>>> items.isnull().head()
   ItemGroupId     I1     I2     I3    I4  ...    I30   I31   I32   I33   I34
0        False  False   True   True  True  ...   True  True  True  True  True
1        False  False  False  False  True  ...   True  True  True  True  True
2        False  False  False   True  True  ...   True  True  True  True  True
3        False  False   True   True  True  ...   True  True  True  True  True
4        False  False  False   True  True  ...   True  True  True  True  True

[5 rows x 35 columns]
>>> 
>>> items.notnull().head()
   ItemGroupId    I1     I2     I3  ...      I31    I32    I33    I34
0         True  True  False  False  ...    False  False  False  False
1         True  True   True   True  ...    False  False  False  False
2         True  True   True  False  ...    False  False  False  False
3         True  True  False  False  ...    False  False  False  False
4         True  True   True  False  ...    False  False  False  False

[5 rows x 35 columns]
>>> 
>>> items.isnull().sum()
ItemGroupId      0
I1               0
I2              46
I3              62
I4              75
I5              84
I6              92
I7              96
I8             113
I9             126
I10            135
I11            142
I12            150
I13            156
I14            166
I15            178
I16            214
I17            228
I18            247
I19            249
I20            251
I21            252
I22            252
I23            252
I24            252
I25            252
I26            254
I27            254
I28            254
I29            254
I30            254
I31            254
I32            255
I33            255
I34            255
dtype: int64
>>> 
>>> items[items.I20.isnull()]
       ItemGroupId       I1         I2         I3 ...   I31  I32  I33  I34
0    1_13069000301  2274736        NaN        NaN ...   NaN  NaN  NaN  NaN
1    1_13069000502  2556261  2556259.0  2556257.0 ...   NaN  NaN  NaN  NaN
2    1_13069000701  2458678  2274748.0        NaN ...   NaN  NaN  NaN  NaN
3    1_13069060001  2274773        NaN        NaN ...   NaN  NaN  NaN  NaN
4    1_13602713301  2366859  2274795.0        NaN ...   NaN  NaN  NaN  NaN
5    1_15326560001  2479975        NaN        NaN ...   NaN  NaN  NaN  NaN
6    1_30235000101  2274876  2274878.0  2274877.0 ...   NaN  NaN  NaN  NaN
7    1_30796060201  2617789  2617788.0  2617787.0 ...   NaN  NaN  NaN  NaN
8    1_30831700301  2275443  2275445.0  2275437.0 ...   NaN  NaN  NaN  NaN
9    1_30849911701  2275607  2275604.0  2275610.0 ...   NaN  NaN  NaN  NaN
10   1_31081110001  2275906  2348465.0  2275908.0 ...   NaN  NaN  NaN  NaN
11   1_31242200301  2479982  2479983.0  2479984.0 ...   NaN  NaN  NaN  NaN
12   1_31242200601  2512435  2512431.0  2512430.0 ...   NaN  NaN  NaN  NaN
13   1_31249813401  2368523        NaN        NaN ...   NaN  NaN  NaN  NaN
14   1_31283400401  2539179  2481204.0  2493149.0 ...   NaN  NaN  NaN  NaN
15   1_31741501301  2721989        NaN        NaN ...   NaN  NaN  NaN  NaN
16   1_31775403901  2643764  2643759.0  2643765.0 ...   NaN  NaN  NaN  NaN
17   1_31842903201  2276763  2276752.0  2276764.0 ...   NaN  NaN  NaN  NaN
18   1_31842904101  2361482        NaN        NaN ...   NaN  NaN  NaN  NaN
19   1_31842930501  2276935  2276934.0  2276936.0 ...   NaN  NaN  NaN  NaN
20   1_32521320501  2720062  2724163.0  2724164.0 ...   NaN  NaN  NaN  NaN
21   1_32521350701  2277194  2277193.0        NaN ...   NaN  NaN  NaN  NaN
22   1_33214802401  2469337        NaN        NaN ...   NaN  NaN  NaN  NaN
23   1_33214810601  2277326  2277329.0  2277328.0 ...   NaN  NaN  NaN  NaN
24   1_33214811601  2469338        NaN        NaN ...   NaN  NaN  NaN  NaN
25   1_33214860801  2277359  2277358.0  2277361.0 ...   NaN  NaN  NaN  NaN
26   1_33255080001  2277582  2277571.0  2277573.0 ...   NaN  NaN  NaN  NaN
27   1_35515210601  2277854        NaN        NaN ...   NaN  NaN  NaN  NaN
28   1_36088400101  2416984  2416983.0  2416982.0 ...   NaN  NaN  NaN  NaN
29   1_37781212301  2721993        NaN        NaN ...   NaN  NaN  NaN  NaN
..             ...      ...        ...        ... ...   ...  ...  ...  ...
225  1_91776861601  2605955  2605965.0  2605964.0 ...   NaN  NaN  NaN  NaN
226  1_91777680101  2398962  2398963.0  2368213.0 ...   NaN  NaN  NaN  NaN
227  1_91779600201  2428134  2428135.0  2428137.0 ...   NaN  NaN  NaN  NaN
228  1_91820620001  2368280  2368284.0  2368286.0 ...   NaN  NaN  NaN  NaN
229  1_91820660001  2428156  2428153.0  2428155.0 ...   NaN  NaN  NaN  NaN
230  1_91820660101  2556720  2556721.0  2556722.0 ...   NaN  NaN  NaN  NaN
231  1_91820700301  2407744  2376189.0  2376192.0 ...   NaN  NaN  NaN  NaN
232  1_91823000301  2362553  2362551.0  2362563.0 ...   NaN  NaN  NaN  NaN
233  1_91823010001  2366676  2366668.0  2366669.0 ...   NaN  NaN  NaN  NaN
234  1_91826400301  2450328  2450327.0  2450322.0 ...   NaN  NaN  NaN  NaN
235  1_91835840001  2421999  2421995.0  2421990.0 ...   NaN  NaN  NaN  NaN
236  1_91971500201  2535866  2535863.0  2535867.0 ...   NaN  NaN  NaN  NaN
237  1_92149040701  2701504  2692249.0  2701502.0 ...   NaN  NaN  NaN  NaN
238  1_92149240001  2382198  2382199.0  2382196.0 ...   NaN  NaN  NaN  NaN
239  1_92151440701  2721271  2726639.0  2724337.0 ...   NaN  NaN  NaN  NaN
240  1_92206510401  2387078        NaN        NaN ...   NaN  NaN  NaN  NaN
241  1_92293340001  2347308  2347304.0  2347303.0 ...   NaN  NaN  NaN  NaN
242  1_92362000701  2347736  2347735.0  2347737.0 ...   NaN  NaN  NaN  NaN
243  1_94206000101  2357672  2357671.0  2407855.0 ...   NaN  NaN  NaN  NaN
244  1_94380640101  2735684  2735683.0  2735686.0 ...   NaN  NaN  NaN  NaN
245  1_AA051200201  2561585  2561583.0  2561586.0 ...   NaN  NaN  NaN  NaN
246  1_AA110900501  2566008  2566010.0  2566013.0 ...   NaN  NaN  NaN  NaN
247  1_AA134772501  2540613  2540614.0  2540612.0 ...   NaN  NaN  NaN  NaN
249  1_AA396600301  2511116  2511111.0  2511113.0 ...   NaN  NaN  NaN  NaN
250  1_AA430201101  2552250  2552243.0  2552251.0 ...   NaN  NaN  NaN  NaN
251  1_AH678800101  2719910  2719909.0  2719912.0 ...   NaN  NaN  NaN  NaN
252  1_AJ202400101  2694263  2694249.0  2694259.0 ...   NaN  NaN  NaN  NaN
253  1_AJ516590101  2723086  2723087.0  2723089.0 ...   NaN  NaN  NaN  NaN
254  1_AJ731601001  2694522  2694521.0  2694524.0 ...   NaN  NaN  NaN  NaN
255  1_DUMMY0SKU01  2216783  2216784.0  2207483.0 ...   NaN  NaN  NaN  NaN

[251 rows x 35 columns]
>>> 
>>> items[items.I2.isnull()]
       ItemGroupId       I1  I2  I3  I4  I5 ...   I29  I30  I31  I32  I33  I34
0    1_13069000301  2274736 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
3    1_13069060001  2274773 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
5    1_15326560001  2479975 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
13   1_31249813401  2368523 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
15   1_31741501301  2721989 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
18   1_31842904101  2361482 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
22   1_33214802401  2469337 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
24   1_33214811601  2469338 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
27   1_35515210601  2277854 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
29   1_37781212301  2721993 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
38   1_52536600201  2721994 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
39   1_53738407501  2406856 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
42   1_55472400901  2280757 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
43   1_55508340401  2473218 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
47   1_58051900201  2373053 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
50   1_59984375901  2740533 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
51   1_59985175901  2740534 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
54   1_61672310201  2282598 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
55   1_61672320101  2361531 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
58   1_64132237101  2740536 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
60   1_64185806101  2740825 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
61   1_64186006101  2740826 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
63   1_64923001101  2740831 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
65   1_65469300301  2539317 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
69   1_70514941001  2556368 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
70   1_70547513001  2460272 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
73   1_72487701201  2460278 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
76   1_74976601401  2289556 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
79   1_80754200201  2740544 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
81   1_81265500501  2682374 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
88   1_81989900701  2298505 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
93   1_82824601901  2740549 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
97   1_83194560101  2301281 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
103  1_83197700101  2735612 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
114  1_84441180801  2309814 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
123  1_84465400401  2311708 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
124  1_84468740001  2741328 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
130  1_84492980101  2315156 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
134  1_84500870001  2351191 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
138  1_84826910001  2318476 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
139  1_84827930001  2318518 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
155  1_85598400101  2324482 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
163  1_86377901401  2683283 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
178  1_87806880201  2333174 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
189  1_88119210001  2335408 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN
240  1_92206510401  2387078 NaN NaN NaN NaN ...   NaN  NaN  NaN  NaN  NaN  NaN

[46 rows x 35 columns]
>>> 
>>> items.shape
(256, 35)
>>> items.dropna(how='any').shape
(1, 35)
>>> items.shape
(256, 35)
>>> items.dropna(how='all').shape
(256, 35)
>>> 
>>> items['I14'].value_counts(dropna=False)
NaN           166
 2421994.0      1
 2280693.0      1
 2545922.0      1
 2705186.0      1
 2723083.0      1
 2535694.0      1
 2322719.0      1
 2366404.0      1
 2503974.0      1
 2347309.0      1
 2561334.0      1
 2686273.0      1
 2718036.0      1
 2540608.0      1
 2345591.0      1
 2321777.0      1
 2311565.0      1
 2392488.0      1
 2552244.0      1
 2535868.0      1
 2334959.0      1
 2309350.0      1
 2330965.0      1
 2713822.0      1
 2718218.0      1
 2565151.0      1
 2435107.0      1
 2611156.0      1
 2692258.0      1
             ... 
 2417655.0      1
 2565057.0      1
 2692037.0      1
 2632657.0      1
 2692053.0      1
 2551772.0      1
 2726672.0      1
 2493150.0      1
 2432239.0      1
 2600667.0      1
 2383345.0      1
 2376186.0      1
 2546184.0      1
 2657839.0      1
 2473520.0      1
 2735696.0      1
 2531911.0      1
 2527819.0      1
 2551797.0      1
 2281064.0      1
 2304621.0      1
 2386550.0      1
 2281121.0      1
 2532011.0      1
 2450096.0      1
 2532021.0      1
 2566007.0      1
 2322124.0      1
 2610901.0      1
 2523621.0      1
Name: I14, Length: 91, dtype: int64
>>> Name: I14, Length: 91, dtype: int64
SyntaxError: invalid syntax
>>> 
>>> items[].fillna(value=0,inplace=True)
SyntaxError: invalid syntax
>>> items[''].fillna(calue=0,inplace=True)
Traceback (most recent call last):
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ''

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    items[''].fillna(calue=0,inplace=True)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\generic.py", line 2489, in _get_item_cache
    values = self._data.get(item)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals.py", line 4115, in get
    loc = self.items.get_loc(item)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ''
>>> items['I1,I2,I3'].fillna(calue=0,inplace=True)
Traceback (most recent call last):
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'I1,I2,I3'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    items['I1,I2,I3'].fillna(calue=0,inplace=True)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\generic.py", line 2489, in _get_item_cache
    values = self._data.get(item)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals.py", line 4115, in get
    loc = self.items.get_loc(item)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'I1,I2,I3'
>>> 	items['I2'].fillna(calue=0,inplace=True)
SyntaxError: unexpected indent
>>> 
>>> 
>>> items['I2'].fillna(calue=0,inplace=True)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    items['I2'].fillna(calue=0,inplace=True)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\series.py", line 3425, in fillna
    **kwargs)
TypeError: fillna() got an unexpected keyword argument 'calue'
>>> items['I2'].fillna(value=0,inplace=True)
>>> items['I2'].value_counts(dropna=False)
0.0          46
2279893.0     1
2726639.0     1
2327984.0     1
2693853.0     1
2312922.0     1
2347735.0     1
2725013.0     1
2532031.0     1
2372278.0     1
2527814.0     1
2450091.0     1
2532004.0     1
2378399.0     1
2419352.0     1
2386564.0     1
2321012.0     1
2330964.0     1
2335329.0     1
2285054.0     1
2531924.0     1
2300573.0     1
2531910.0     1
2546173.0     1
2718177.0     1
2398963.0     1
2286342.0     1
2464529.0     1
2605965.0     1
2278370.0     1
             ..
2481204.0     1
2370611.0     1
2735683.0     1
2280688.0     1
2311415.0     1
2428153.0     1
2276752.0     1
2407660.0     1
2362850.0     1
2723284.0     1
2383313.0     1
2424043.0     1
2373057.0     1
2342334.0     1
2348465.0     1
2315690.0     1
2311589.0     1
2694521.0     1
2483464.0     1
2561583.0     1
2321769.0     1
2293064.0     1
2301246.0     1
2315575.0     1
2561329.0     1
2503976.0     1
2701431.0     1
2342167.0     1
2723087.0     1
2694129.0     1
Name: I2, Length: 211, dtype: int64
>>> Name: I2, Length: 211, dtype: int64
SyntaxError: invalid syntax
>>> 
>>> items.shape
(256, 35)
>>> items['I3','I4'].fillna(Value=0,inplace=True)
Traceback (most recent call last):
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('I3', 'I4')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    items['I3','I4'].fillna(Value=0,inplace=True)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\generic.py", line 2489, in _get_item_cache
    values = self._data.get(item)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals.py", line 4115, in get
    loc = self.items.get_loc(item)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('I3', 'I4')
>>> 
>>> type(items)
<class 'pandas.core.frame.DataFrame'>
>>> items.update(items[['I2','I3','I4','I5']].fillna(0))
>>> items.head()
     ItemGroupId       I1         I2         I3 ...   I31  I32  I33  I34
0  1_13069000301  2274736        0.0        0.0 ...   NaN  NaN  NaN  NaN
1  1_13069000502  2556261  2556259.0  2556257.0 ...   NaN  NaN  NaN  NaN
2  1_13069000701  2458678  2274748.0        0.0 ...   NaN  NaN  NaN  NaN
3  1_13069060001  2274773        0.0        0.0 ...   NaN  NaN  NaN  NaN
4  1_13602713301  2366859  2274795.0        0.0 ...   NaN  NaN  NaN  NaN

[5 rows x 35 columns]
>>> [5 rows x 35 columns]
SyntaxError: invalid syntax
>>> 
>>> items.update(items[[]].fillna(0))
>>> items
       ItemGroupId       I1         I2         I3 ...   I31  I32  I33  I34
0    1_13069000301  2274736        0.0        0.0 ...   NaN  NaN  NaN  NaN
1    1_13069000502  2556261  2556259.0  2556257.0 ...   NaN  NaN  NaN  NaN
2    1_13069000701  2458678  2274748.0        0.0 ...   NaN  NaN  NaN  NaN
3    1_13069060001  2274773        0.0        0.0 ...   NaN  NaN  NaN  NaN
4    1_13602713301  2366859  2274795.0        0.0 ...   NaN  NaN  NaN  NaN
5    1_15326560001  2479975        0.0        0.0 ...   NaN  NaN  NaN  NaN
6    1_30235000101  2274876  2274878.0  2274877.0 ...   NaN  NaN  NaN  NaN
7    1_30796060201  2617789  2617788.0  2617787.0 ...   NaN  NaN  NaN  NaN
8    1_30831700301  2275443  2275445.0  2275437.0 ...   NaN  NaN  NaN  NaN
9    1_30849911701  2275607  2275604.0  2275610.0 ...   NaN  NaN  NaN  NaN
10   1_31081110001  2275906  2348465.0  2275908.0 ...   NaN  NaN  NaN  NaN
11   1_31242200301  2479982  2479983.0  2479984.0 ...   NaN  NaN  NaN  NaN
12   1_31242200601  2512435  2512431.0  2512430.0 ...   NaN  NaN  NaN  NaN
13   1_31249813401  2368523        0.0        0.0 ...   NaN  NaN  NaN  NaN
14   1_31283400401  2539179  2481204.0  2493149.0 ...   NaN  NaN  NaN  NaN
15   1_31741501301  2721989        0.0        0.0 ...   NaN  NaN  NaN  NaN
16   1_31775403901  2643764  2643759.0  2643765.0 ...   NaN  NaN  NaN  NaN
17   1_31842903201  2276763  2276752.0  2276764.0 ...   NaN  NaN  NaN  NaN
18   1_31842904101  2361482        0.0        0.0 ...   NaN  NaN  NaN  NaN
19   1_31842930501  2276935  2276934.0  2276936.0 ...   NaN  NaN  NaN  NaN
20   1_32521320501  2720062  2724163.0  2724164.0 ...   NaN  NaN  NaN  NaN
21   1_32521350701  2277194  2277193.0        0.0 ...   NaN  NaN  NaN  NaN
22   1_33214802401  2469337        0.0        0.0 ...   NaN  NaN  NaN  NaN
23   1_33214810601  2277326  2277329.0  2277328.0 ...   NaN  NaN  NaN  NaN
24   1_33214811601  2469338        0.0        0.0 ...   NaN  NaN  NaN  NaN
25   1_33214860801  2277359  2277358.0  2277361.0 ...   NaN  NaN  NaN  NaN
26   1_33255080001  2277582  2277571.0  2277573.0 ...   NaN  NaN  NaN  NaN
27   1_35515210601  2277854        0.0        0.0 ...   NaN  NaN  NaN  NaN
28   1_36088400101  2416984  2416983.0  2416982.0 ...   NaN  NaN  NaN  NaN
29   1_37781212301  2721993        0.0        0.0 ...   NaN  NaN  NaN  NaN
..             ...      ...        ...        ... ...   ...  ...  ...  ...
226  1_91777680101  2398962  2398963.0  2368213.0 ...   NaN  NaN  NaN  NaN
227  1_91779600201  2428134  2428135.0  2428137.0 ...   NaN  NaN  NaN  NaN
228  1_91820620001  2368280  2368284.0  2368286.0 ...   NaN  NaN  NaN  NaN
229  1_91820660001  2428156  2428153.0  2428155.0 ...   NaN  NaN  NaN  NaN
230  1_91820660101  2556720  2556721.0  2556722.0 ...   NaN  NaN  NaN  NaN
231  1_91820700301  2407744  2376189.0  2376192.0 ...   NaN  NaN  NaN  NaN
232  1_91823000301  2362553  2362551.0  2362563.0 ...   NaN  NaN  NaN  NaN
233  1_91823010001  2366676  2366668.0  2366669.0 ...   NaN  NaN  NaN  NaN
234  1_91826400301  2450328  2450327.0  2450322.0 ...   NaN  NaN  NaN  NaN
235  1_91835840001  2421999  2421995.0  2421990.0 ...   NaN  NaN  NaN  NaN
236  1_91971500201  2535866  2535863.0  2535867.0 ...   NaN  NaN  NaN  NaN
237  1_92149040701  2701504  2692249.0  2701502.0 ...   NaN  NaN  NaN  NaN
238  1_92149240001  2382198  2382199.0  2382196.0 ...   NaN  NaN  NaN  NaN
239  1_92151440701  2721271  2726639.0  2724337.0 ...   NaN  NaN  NaN  NaN
240  1_92206510401  2387078        0.0        0.0 ...   NaN  NaN  NaN  NaN
241  1_92293340001  2347308  2347304.0  2347303.0 ...   NaN  NaN  NaN  NaN
242  1_92362000701  2347736  2347735.0  2347737.0 ...   NaN  NaN  NaN  NaN
243  1_94206000101  2357672  2357671.0  2407855.0 ...   NaN  NaN  NaN  NaN
244  1_94380640101  2735684  2735683.0  2735686.0 ...   NaN  NaN  NaN  NaN
245  1_AA051200201  2561585  2561583.0  2561586.0 ...   NaN  NaN  NaN  NaN
246  1_AA110900501  2566008  2566010.0  2566013.0 ...   NaN  NaN  NaN  NaN
247  1_AA134772501  2540613  2540614.0  2540612.0 ...   NaN  NaN  NaN  NaN
248  1_AA249410601  2726673  2722985.0  2722982.0 ...   NaN  NaN  NaN  NaN
249  1_AA396600301  2511116  2511111.0  2511113.0 ...   NaN  NaN  NaN  NaN
250  1_AA430201101  2552250  2552243.0  2552251.0 ...   NaN  NaN  NaN  NaN
251  1_AH678800101  2719910  2719909.0  2719912.0 ...   NaN  NaN  NaN  NaN
252  1_AJ202400101  2694263  2694249.0  2694259.0 ...   NaN  NaN  NaN  NaN
253  1_AJ516590101  2723086  2723087.0  2723089.0 ...   NaN  NaN  NaN  NaN
254  1_AJ731601001  2694522  2694521.0  2694524.0 ...   NaN  NaN  NaN  NaN
255  1_DUMMY0SKU01  2216783  2216784.0  2207483.0 ...   NaN  NaN  NaN  NaN

[256 rows x 35 columns]
>>> 
>>> items.update(items[[0:255,:]].fillna(0))
SyntaxError: invalid syntax
>>> items.update(items[[,:]].fillna(0))
SyntaxError: invalid syntax
>>> items.update(items[[(0:255),:]].fillna(0))
SyntaxError: invalid syntax
>>> 
>>> 
>>> items.update(items[['I6',	'I7',	'I8',	'I9',	'I10',	'I11',	'I12',	'I13',	'I14',	'I15',	'I16',	'I17',	'I18',	'I19',	'I20',	'I21',	'I22',	'I23',	'I24',	'I25',	'I26',	'I27',	'I28',	'I29',	'I30',	'I31',	'I32',	'I33',	'I34',	'I35']].fillna(0))
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    items.update(items[['I6',	'I7',	'I8',	'I9',	'I10',	'I11',	'I12',	'I13',	'I14',	'I15',	'I16',	'I17',	'I18',	'I19',	'I20',	'I21',	'I22',	'I23',	'I24',	'I25',	'I26',	'I27',	'I28',	'I29',	'I30',	'I31',	'I32',	'I33',	'I34',	'I35']].fillna(0))
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2682, in __getitem__
    return self._getitem_array(key)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2726, in _getitem_array
    indexer = self.loc._convert_to_indexer(key, axis=1)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1327, in _convert_to_indexer
    .format(mask=objarr[mask]))
KeyError: "['I35'] not in index"
>>> items.update(items[['I6','I7','I8','I9','I10','I11','I12','I13','I14','I15','I16','I17','I18','I19','I20','I21','I22','I23','I24','I25','I26','I27','I28','I29','I30','I31','I32','I33','I34','I35']].fillna(0))
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    items.update(items[['I6','I7','I8','I9','I10','I11','I12','I13','I14','I15','I16','I17','I18','I19','I20','I21','I22','I23','I24','I25','I26','I27','I28','I29','I30','I31','I32','I33','I34','I35']].fillna(0))
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2682, in __getitem__
    return self._getitem_array(key)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2726, in _getitem_array
    indexer = self.loc._convert_to_indexer(key, axis=1)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1327, in _convert_to_indexer
    .format(mask=objarr[mask]))
KeyError: "['I35'] not in index"
>>> 
>>> items.update(items[['I6','I7','I8','I9','I10','I11','I12','I13','I14','I15','I16','I17','I18','I19','I20','I21','I22','I23','I24','I25','I26','I27','I28','I29','I30','I31','I32','I33','I34']].fillna(0))
>>> items[,20:29]
SyntaxError: invalid syntax
>>> items
       ItemGroupId       I1         I2         I3 ...   I31  I32  I33  I34
0    1_13069000301  2274736        0.0        0.0 ...   0.0  0.0  0.0  0.0
1    1_13069000502  2556261  2556259.0  2556257.0 ...   0.0  0.0  0.0  0.0
2    1_13069000701  2458678  2274748.0        0.0 ...   0.0  0.0  0.0  0.0
3    1_13069060001  2274773        0.0        0.0 ...   0.0  0.0  0.0  0.0
4    1_13602713301  2366859  2274795.0        0.0 ...   0.0  0.0  0.0  0.0
5    1_15326560001  2479975        0.0        0.0 ...   0.0  0.0  0.0  0.0
6    1_30235000101  2274876  2274878.0  2274877.0 ...   0.0  0.0  0.0  0.0
7    1_30796060201  2617789  2617788.0  2617787.0 ...   0.0  0.0  0.0  0.0
8    1_30831700301  2275443  2275445.0  2275437.0 ...   0.0  0.0  0.0  0.0
9    1_30849911701  2275607  2275604.0  2275610.0 ...   0.0  0.0  0.0  0.0
10   1_31081110001  2275906  2348465.0  2275908.0 ...   0.0  0.0  0.0  0.0
11   1_31242200301  2479982  2479983.0  2479984.0 ...   0.0  0.0  0.0  0.0
12   1_31242200601  2512435  2512431.0  2512430.0 ...   0.0  0.0  0.0  0.0
13   1_31249813401  2368523        0.0        0.0 ...   0.0  0.0  0.0  0.0
14   1_31283400401  2539179  2481204.0  2493149.0 ...   0.0  0.0  0.0  0.0
15   1_31741501301  2721989        0.0        0.0 ...   0.0  0.0  0.0  0.0
16   1_31775403901  2643764  2643759.0  2643765.0 ...   0.0  0.0  0.0  0.0
17   1_31842903201  2276763  2276752.0  2276764.0 ...   0.0  0.0  0.0  0.0
18   1_31842904101  2361482        0.0        0.0 ...   0.0  0.0  0.0  0.0
19   1_31842930501  2276935  2276934.0  2276936.0 ...   0.0  0.0  0.0  0.0
20   1_32521320501  2720062  2724163.0  2724164.0 ...   0.0  0.0  0.0  0.0
21   1_32521350701  2277194  2277193.0        0.0 ...   0.0  0.0  0.0  0.0
22   1_33214802401  2469337        0.0        0.0 ...   0.0  0.0  0.0  0.0
23   1_33214810601  2277326  2277329.0  2277328.0 ...   0.0  0.0  0.0  0.0
24   1_33214811601  2469338        0.0        0.0 ...   0.0  0.0  0.0  0.0
25   1_33214860801  2277359  2277358.0  2277361.0 ...   0.0  0.0  0.0  0.0
26   1_33255080001  2277582  2277571.0  2277573.0 ...   0.0  0.0  0.0  0.0
27   1_35515210601  2277854        0.0        0.0 ...   0.0  0.0  0.0  0.0
28   1_36088400101  2416984  2416983.0  2416982.0 ...   0.0  0.0  0.0  0.0
29   1_37781212301  2721993        0.0        0.0 ...   0.0  0.0  0.0  0.0
..             ...      ...        ...        ... ...   ...  ...  ...  ...
226  1_91777680101  2398962  2398963.0  2368213.0 ...   0.0  0.0  0.0  0.0
227  1_91779600201  2428134  2428135.0  2428137.0 ...   0.0  0.0  0.0  0.0
228  1_91820620001  2368280  2368284.0  2368286.0 ...   0.0  0.0  0.0  0.0
229  1_91820660001  2428156  2428153.0  2428155.0 ...   0.0  0.0  0.0  0.0
230  1_91820660101  2556720  2556721.0  2556722.0 ...   0.0  0.0  0.0  0.0
231  1_91820700301  2407744  2376189.0  2376192.0 ...   0.0  0.0  0.0  0.0
232  1_91823000301  2362553  2362551.0  2362563.0 ...   0.0  0.0  0.0  0.0
233  1_91823010001  2366676  2366668.0  2366669.0 ...   0.0  0.0  0.0  0.0
234  1_91826400301  2450328  2450327.0  2450322.0 ...   0.0  0.0  0.0  0.0
235  1_91835840001  2421999  2421995.0  2421990.0 ...   0.0  0.0  0.0  0.0
236  1_91971500201  2535866  2535863.0  2535867.0 ...   0.0  0.0  0.0  0.0
237  1_92149040701  2701504  2692249.0  2701502.0 ...   0.0  0.0  0.0  0.0
238  1_92149240001  2382198  2382199.0  2382196.0 ...   0.0  0.0  0.0  0.0
239  1_92151440701  2721271  2726639.0  2724337.0 ...   0.0  0.0  0.0  0.0
240  1_92206510401  2387078        0.0        0.0 ...   0.0  0.0  0.0  0.0
241  1_92293340001  2347308  2347304.0  2347303.0 ...   0.0  0.0  0.0  0.0
242  1_92362000701  2347736  2347735.0  2347737.0 ...   0.0  0.0  0.0  0.0
243  1_94206000101  2357672  2357671.0  2407855.0 ...   0.0  0.0  0.0  0.0
244  1_94380640101  2735684  2735683.0  2735686.0 ...   0.0  0.0  0.0  0.0
245  1_AA051200201  2561585  2561583.0  2561586.0 ...   0.0  0.0  0.0  0.0
246  1_AA110900501  2566008  2566010.0  2566013.0 ...   0.0  0.0  0.0  0.0
247  1_AA134772501  2540613  2540614.0  2540612.0 ...   0.0  0.0  0.0  0.0
248  1_AA249410601  2726673  2722985.0  2722982.0 ...   0.0  0.0  0.0  0.0
249  1_AA396600301  2511116  2511111.0  2511113.0 ...   0.0  0.0  0.0  0.0
250  1_AA430201101  2552250  2552243.0  2552251.0 ...   0.0  0.0  0.0  0.0
251  1_AH678800101  2719910  2719909.0  2719912.0 ...   0.0  0.0  0.0  0.0
252  1_AJ202400101  2694263  2694249.0  2694259.0 ...   0.0  0.0  0.0  0.0
253  1_AJ516590101  2723086  2723087.0  2723089.0 ...   0.0  0.0  0.0  0.0
254  1_AJ731601001  2694522  2694521.0  2694524.0 ...   0.0  0.0  0.0  0.0
255  1_DUMMY0SKU01  2216783  2216784.0  2207483.0 ...   0.0  0.0  0.0  0.0

[256 rows x 35 columns]
>>> 
>>> writer = pd.ExcelWriter('iga.xlsx, engine= 'xlsxwriter'
			    
SyntaxError: invalid syntax
>>> 
			    
>>> pd.to_excel("iga.xlsx", sheet_name="IGA_ITEMS")
			    
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    pd.to_excel("iga.xlsx", sheet_name="IGA_ITEMS")
AttributeError: module 'pandas' has no attribute 'to_excel'
>>> 
			    
>>> import pandas as pd
			    
>>> df.to_excel("iga.xlsx", sheet_name="IGA_ITEMS")
			    
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    df.to_excel("iga.xlsx", sheet_name="IGA_ITEMS")
NameError: name 'df' is not defined
>>> items.to_excel("iga.xlsx", sheet_name="IGA_ITEMS")
			    
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    items.to_excel("iga.xlsx", sheet_name="IGA_ITEMS")
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 1766, in to_excel
    engine=engine)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\io\formats\excel.py", line 654, in write
    writer.save()
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\io\excel.py", line 1732, in save
    return self.book.close()
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\xlsxwriter\workbook.py", line 311, in close
    self._store_workbook()
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\xlsxwriter\workbook.py", line 640, in _store_workbook
    allowZip64=self.allow_zip64)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\zipfile.py", line 1090, in __init__
    self.fp = io.open(file, filemode)
PermissionError: [Errno 13] Permission denied: 'iga.xlsx'
>>> 
>>> 
>>> items.to_excel("iga.xlsx", sheet_name="IGA_ITEMS")
>>> 
>>> items.isnull()
     ItemGroupId     I1     I2     I3  ...      I31    I32    I33    I34
0          False  False  False  False  ...    False  False  False  False
1          False  False  False  False  ...    False  False  False  False
2          False  False  False  False  ...    False  False  False  False
3          False  False  False  False  ...    False  False  False  False
4          False  False  False  False  ...    False  False  False  False
5          False  False  False  False  ...    False  False  False  False
6          False  False  False  False  ...    False  False  False  False
7          False  False  False  False  ...    False  False  False  False
8          False  False  False  False  ...    False  False  False  False
9          False  False  False  False  ...    False  False  False  False
10         False  False  False  False  ...    False  False  False  False
11         False  False  False  False  ...    False  False  False  False
12         False  False  False  False  ...    False  False  False  False
13         False  False  False  False  ...    False  False  False  False
14         False  False  False  False  ...    False  False  False  False
15         False  False  False  False  ...    False  False  False  False
16         False  False  False  False  ...    False  False  False  False
17         False  False  False  False  ...    False  False  False  False
18         False  False  False  False  ...    False  False  False  False
19         False  False  False  False  ...    False  False  False  False
20         False  False  False  False  ...    False  False  False  False
21         False  False  False  False  ...    False  False  False  False
22         False  False  False  False  ...    False  False  False  False
23         False  False  False  False  ...    False  False  False  False
24         False  False  False  False  ...    False  False  False  False
25         False  False  False  False  ...    False  False  False  False
26         False  False  False  False  ...    False  False  False  False
27         False  False  False  False  ...    False  False  False  False
28         False  False  False  False  ...    False  False  False  False
29         False  False  False  False  ...    False  False  False  False
..           ...    ...    ...    ...  ...      ...    ...    ...    ...
226        False  False  False  False  ...    False  False  False  False
227        False  False  False  False  ...    False  False  False  False
228        False  False  False  False  ...    False  False  False  False
229        False  False  False  False  ...    False  False  False  False
230        False  False  False  False  ...    False  False  False  False
231        False  False  False  False  ...    False  False  False  False
232        False  False  False  False  ...    False  False  False  False
233        False  False  False  False  ...    False  False  False  False
234        False  False  False  False  ...    False  False  False  False
235        False  False  False  False  ...    False  False  False  False
236        False  False  False  False  ...    False  False  False  False
237        False  False  False  False  ...    False  False  False  False
238        False  False  False  False  ...    False  False  False  False
239        False  False  False  False  ...    False  False  False  False
240        False  False  False  False  ...    False  False  False  False
241        False  False  False  False  ...    False  False  False  False
242        False  False  False  False  ...    False  False  False  False
243        False  False  False  False  ...    False  False  False  False
244        False  False  False  False  ...    False  False  False  False
245        False  False  False  False  ...    False  False  False  False
246        False  False  False  False  ...    False  False  False  False
247        False  False  False  False  ...    False  False  False  False
248        False  False  False  False  ...    False  False  False  False
249        False  False  False  False  ...    False  False  False  False
250        False  False  False  False  ...    False  False  False  False
251        False  False  False  False  ...    False  False  False  False
252        False  False  False  False  ...    False  False  False  False
253        False  False  False  False  ...    False  False  False  False
254        False  False  False  False  ...    False  False  False  False
255        False  False  False  False  ...    False  False  False  False

[256 rows x 35 columns]
>>>  >items
SyntaxError: unexpected indent
>>> 
>>> items
       ItemGroupId       I1         I2         I3 ...   I31  I32  I33  I34
0    1_13069000301  2274736        0.0        0.0 ...   0.0  0.0  0.0  0.0
1    1_13069000502  2556261  2556259.0  2556257.0 ...   0.0  0.0  0.0  0.0
2    1_13069000701  2458678  2274748.0        0.0 ...   0.0  0.0  0.0  0.0
3    1_13069060001  2274773        0.0        0.0 ...   0.0  0.0  0.0  0.0
4    1_13602713301  2366859  2274795.0        0.0 ...   0.0  0.0  0.0  0.0
5    1_15326560001  2479975        0.0        0.0 ...   0.0  0.0  0.0  0.0
6    1_30235000101  2274876  2274878.0  2274877.0 ...   0.0  0.0  0.0  0.0
7    1_30796060201  2617789  2617788.0  2617787.0 ...   0.0  0.0  0.0  0.0
8    1_30831700301  2275443  2275445.0  2275437.0 ...   0.0  0.0  0.0  0.0
9    1_30849911701  2275607  2275604.0  2275610.0 ...   0.0  0.0  0.0  0.0
10   1_31081110001  2275906  2348465.0  2275908.0 ...   0.0  0.0  0.0  0.0
11   1_31242200301  2479982  2479983.0  2479984.0 ...   0.0  0.0  0.0  0.0
12   1_31242200601  2512435  2512431.0  2512430.0 ...   0.0  0.0  0.0  0.0
13   1_31249813401  2368523        0.0        0.0 ...   0.0  0.0  0.0  0.0
14   1_31283400401  2539179  2481204.0  2493149.0 ...   0.0  0.0  0.0  0.0
15   1_31741501301  2721989        0.0        0.0 ...   0.0  0.0  0.0  0.0
16   1_31775403901  2643764  2643759.0  2643765.0 ...   0.0  0.0  0.0  0.0
17   1_31842903201  2276763  2276752.0  2276764.0 ...   0.0  0.0  0.0  0.0
18   1_31842904101  2361482        0.0        0.0 ...   0.0  0.0  0.0  0.0
19   1_31842930501  2276935  2276934.0  2276936.0 ...   0.0  0.0  0.0  0.0
20   1_32521320501  2720062  2724163.0  2724164.0 ...   0.0  0.0  0.0  0.0
21   1_32521350701  2277194  2277193.0        0.0 ...   0.0  0.0  0.0  0.0
22   1_33214802401  2469337        0.0        0.0 ...   0.0  0.0  0.0  0.0
23   1_33214810601  2277326  2277329.0  2277328.0 ...   0.0  0.0  0.0  0.0
24   1_33214811601  2469338        0.0        0.0 ...   0.0  0.0  0.0  0.0
25   1_33214860801  2277359  2277358.0  2277361.0 ...   0.0  0.0  0.0  0.0
26   1_33255080001  2277582  2277571.0  2277573.0 ...   0.0  0.0  0.0  0.0
27   1_35515210601  2277854        0.0        0.0 ...   0.0  0.0  0.0  0.0
28   1_36088400101  2416984  2416983.0  2416982.0 ...   0.0  0.0  0.0  0.0
29   1_37781212301  2721993        0.0        0.0 ...   0.0  0.0  0.0  0.0
..             ...      ...        ...        ... ...   ...  ...  ...  ...
226  1_91777680101  2398962  2398963.0  2368213.0 ...   0.0  0.0  0.0  0.0
227  1_91779600201  2428134  2428135.0  2428137.0 ...   0.0  0.0  0.0  0.0
228  1_91820620001  2368280  2368284.0  2368286.0 ...   0.0  0.0  0.0  0.0
229  1_91820660001  2428156  2428153.0  2428155.0 ...   0.0  0.0  0.0  0.0
230  1_91820660101  2556720  2556721.0  2556722.0 ...   0.0  0.0  0.0  0.0
231  1_91820700301  2407744  2376189.0  2376192.0 ...   0.0  0.0  0.0  0.0
232  1_91823000301  2362553  2362551.0  2362563.0 ...   0.0  0.0  0.0  0.0
233  1_91823010001  2366676  2366668.0  2366669.0 ...   0.0  0.0  0.0  0.0
234  1_91826400301  2450328  2450327.0  2450322.0 ...   0.0  0.0  0.0  0.0
235  1_91835840001  2421999  2421995.0  2421990.0 ...   0.0  0.0  0.0  0.0
236  1_91971500201  2535866  2535863.0  2535867.0 ...   0.0  0.0  0.0  0.0
237  1_92149040701  2701504  2692249.0  2701502.0 ...   0.0  0.0  0.0  0.0
238  1_92149240001  2382198  2382199.0  2382196.0 ...   0.0  0.0  0.0  0.0
239  1_92151440701  2721271  2726639.0  2724337.0 ...   0.0  0.0  0.0  0.0
240  1_92206510401  2387078        0.0        0.0 ...   0.0  0.0  0.0  0.0
241  1_92293340001  2347308  2347304.0  2347303.0 ...   0.0  0.0  0.0  0.0
242  1_92362000701  2347736  2347735.0  2347737.0 ...   0.0  0.0  0.0  0.0
243  1_94206000101  2357672  2357671.0  2407855.0 ...   0.0  0.0  0.0  0.0
244  1_94380640101  2735684  2735683.0  2735686.0 ...   0.0  0.0  0.0  0.0
245  1_AA051200201  2561585  2561583.0  2561586.0 ...   0.0  0.0  0.0  0.0
246  1_AA110900501  2566008  2566010.0  2566013.0 ...   0.0  0.0  0.0  0.0
247  1_AA134772501  2540613  2540614.0  2540612.0 ...   0.0  0.0  0.0  0.0
248  1_AA249410601  2726673  2722985.0  2722982.0 ...   0.0  0.0  0.0  0.0
249  1_AA396600301  2511116  2511111.0  2511113.0 ...   0.0  0.0  0.0  0.0
250  1_AA430201101  2552250  2552243.0  2552251.0 ...   0.0  0.0  0.0  0.0
251  1_AH678800101  2719910  2719909.0  2719912.0 ...   0.0  0.0  0.0  0.0
252  1_AJ202400101  2694263  2694249.0  2694259.0 ...   0.0  0.0  0.0  0.0
253  1_AJ516590101  2723086  2723087.0  2723089.0 ...   0.0  0.0  0.0  0.0
254  1_AJ731601001  2694522  2694521.0  2694524.0 ...   0.0  0.0  0.0  0.0
255  1_DUMMY0SKU01  2216783  2216784.0  2207483.0 ...   0.0  0.0  0.0  0.0

[256 rows x 35 columns]
>>> type(items[,1])
SyntaxError: invalid syntax
>>> type(items[:,1])
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    type(items[:,1])
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\generic.py", line 2487, in _get_item_cache
    res = cache.get(item)
TypeError: unhashable type: 'slice'
>>> 
>>> items.loc[:,[I1,I2]]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    items.loc[:,[I1,I2]]
NameError: name 'I1' is not defined
>>> 
>>> items.loc[:,[1]]
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    items.loc[:,[1]]
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1472, in __getitem__
    return self._getitem_tuple(key)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 890, in _getitem_tuple
    retval = getattr(retval, self.name)._getitem_axis(key, axis=i)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1901, in _getitem_axis
    return self._getitem_iterable(key, axis=axis)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1143, in _getitem_iterable
    self._validate_read_indexer(key, indexer, axis)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1206, in _validate_read_indexer
    key=key, axis=self.obj._get_axis_name(axis)))
KeyError: 'None of [[1]] are in the [columns]'
>>> items.loc[:,['I2','I3']]
            I2         I3
0          0.0        0.0
1    2556259.0  2556257.0
2    2274748.0        0.0
3          0.0        0.0
4    2274795.0        0.0
5          0.0        0.0
6    2274878.0  2274877.0
7    2617788.0  2617787.0
8    2275445.0  2275437.0
9    2275604.0  2275610.0
10   2348465.0  2275908.0
11   2479983.0  2479984.0
12   2512431.0  2512430.0
13         0.0        0.0
14   2481204.0  2493149.0
15         0.0        0.0
16   2643759.0  2643765.0
17   2276752.0  2276764.0
18         0.0        0.0
19   2276934.0  2276936.0
20   2724163.0  2724164.0
21   2277193.0        0.0
22         0.0        0.0
23   2277329.0  2277328.0
24         0.0        0.0
25   2277358.0  2277361.0
26   2277571.0  2277573.0
27         0.0        0.0
28   2416983.0  2416982.0
29         0.0        0.0
..         ...        ...
226  2398963.0  2368213.0
227  2428135.0  2428137.0
228  2368284.0  2368286.0
229  2428153.0  2428155.0
230  2556721.0  2556722.0
231  2376189.0  2376192.0
232  2362551.0  2362563.0
233  2366668.0  2366669.0
234  2450327.0  2450322.0
235  2421995.0  2421990.0
236  2535863.0  2535867.0
237  2692249.0  2701502.0
238  2382199.0  2382196.0
239  2726639.0  2724337.0
240        0.0        0.0
241  2347304.0  2347303.0
242  2347735.0  2347737.0
243  2357671.0  2407855.0
244  2735683.0  2735686.0
245  2561583.0  2561586.0
246  2566010.0  2566013.0
247  2540614.0  2540612.0
248  2722985.0  2722982.0
249  2511111.0  2511113.0
250  2552243.0  2552251.0
251  2719909.0  2719912.0
252  2694249.0  2694259.0
253  2723087.0  2723089.0
254  2694521.0  2694524.0
255  2216784.0  2207483.0

[256 rows x 2 columns]
>>>  items.loc[:,['I2':'I34']]
SyntaxError: unexpected indent
>>> 
>>> items.loc[:,['I2':'I34']]
SyntaxError: invalid syntax
>>> 
>>> items.loc[:,'I2':'I34']
            I2         I3         I4         I5 ...   I31  I32  I33  I34
0          0.0        0.0        0.0        0.0 ...   0.0  0.0  0.0  0.0
1    2556259.0  2556257.0        0.0        0.0 ...   0.0  0.0  0.0  0.0
2    2274748.0        0.0        0.0        0.0 ...   0.0  0.0  0.0  0.0
3          0.0        0.0        0.0        0.0 ...   0.0  0.0  0.0  0.0
4    2274795.0        0.0        0.0        0.0 ...   0.0  0.0  0.0  0.0
5          0.0        0.0        0.0        0.0 ...   0.0  0.0  0.0  0.0
6    2274878.0  2274877.0  2469311.0  2274879.0 ...   0.0  0.0  0.0  0.0
7    2617788.0  2617787.0  2617790.0  2691882.0 ...   0.0  0.0  0.0  0.0
8    2275445.0  2275437.0  2275434.0  2275436.0 ...   0.0  0.0  0.0  0.0
9    2275604.0  2275610.0  2275609.0  2275603.0 ...   0.0  0.0  0.0  0.0
10   2348465.0  2275908.0  2275905.0  2275904.0 ...   0.0  0.0  0.0  0.0
11   2479983.0  2479984.0  2479985.0  2479986.0 ...   0.0  0.0  0.0  0.0
12   2512431.0  2512430.0  2512429.0  2512434.0 ...   0.0  0.0  0.0  0.0
13         0.0        0.0        0.0        0.0 ...   0.0  0.0  0.0  0.0
14   2481204.0  2493149.0  2493155.0  2539180.0 ...   0.0  0.0  0.0  0.0
15         0.0        0.0        0.0        0.0 ...   0.0  0.0  0.0  0.0
16   2643759.0  2643765.0  2643762.0  2643761.0 ...   0.0  0.0  0.0  0.0
17   2276752.0  2276764.0  2276754.0        0.0 ...   0.0  0.0  0.0  0.0
18         0.0        0.0        0.0        0.0 ...   0.0  0.0  0.0  0.0
19   2276934.0  2276936.0  2276944.0  2276942.0 ...   0.0  0.0  0.0  0.0
20   2724163.0  2724164.0  2724165.0  2724166.0 ...   0.0  0.0  0.0  0.0
21   2277193.0        0.0        0.0        0.0 ...   0.0  0.0  0.0  0.0
22         0.0        0.0        0.0        0.0 ...   0.0  0.0  0.0  0.0
23   2277329.0  2277328.0  2277330.0  2277327.0 ...   0.0  0.0  0.0  0.0
24         0.0        0.0        0.0        0.0 ...   0.0  0.0  0.0  0.0
25   2277358.0  2277361.0  2277362.0  2277364.0 ...   0.0  0.0  0.0  0.0
26   2277571.0  2277573.0  2277576.0  2277578.0 ...   0.0  0.0  0.0  0.0
27         0.0        0.0        0.0        0.0 ...   0.0  0.0  0.0  0.0
28   2416983.0  2416982.0  2416979.0  2416980.0 ...   0.0  0.0  0.0  0.0
29         0.0        0.0        0.0        0.0 ...   0.0  0.0  0.0  0.0
..         ...        ...        ...        ... ...   ...  ...  ...  ...
226  2398963.0  2368213.0  2368216.0  2368217.0 ...   0.0  0.0  0.0  0.0
227  2428135.0  2428137.0  2428139.0  2428136.0 ...   0.0  0.0  0.0  0.0
228  2368284.0  2368286.0  2368281.0  2368285.0 ...   0.0  0.0  0.0  0.0
229  2428153.0  2428155.0  2428145.0  2428140.0 ...   0.0  0.0  0.0  0.0
230  2556721.0  2556722.0  2556724.0  2556714.0 ...   0.0  0.0  0.0  0.0
231  2376189.0  2376192.0  2376197.0  2376198.0 ...   0.0  0.0  0.0  0.0
232  2362551.0  2362563.0  2362555.0  2362560.0 ...   0.0  0.0  0.0  0.0
233  2366668.0  2366669.0  2366670.0  2366671.0 ...   0.0  0.0  0.0  0.0
234  2450327.0  2450322.0  2450330.0  2450326.0 ...   0.0  0.0  0.0  0.0
235  2421995.0  2421990.0  2421988.0  2421985.0 ...   0.0  0.0  0.0  0.0
236  2535863.0  2535867.0  2535864.0  2535862.0 ...   0.0  0.0  0.0  0.0
237  2692249.0  2701502.0  2701503.0  2692251.0 ...   0.0  0.0  0.0  0.0
238  2382199.0  2382196.0        0.0        0.0 ...   0.0  0.0  0.0  0.0
239  2726639.0  2724337.0  2724336.0  2713823.0 ...   0.0  0.0  0.0  0.0
240        0.0        0.0        0.0        0.0 ...   0.0  0.0  0.0  0.0
241  2347304.0  2347303.0  2347314.0  2347313.0 ...   0.0  0.0  0.0  0.0
242  2347735.0  2347737.0  2347739.0  2347744.0 ...   0.0  0.0  0.0  0.0
243  2357671.0  2407855.0  2357665.0  2357666.0 ...   0.0  0.0  0.0  0.0
244  2735683.0  2735686.0  2735688.0  2735687.0 ...   0.0  0.0  0.0  0.0
245  2561583.0  2561586.0  2561584.0  2561576.0 ...   0.0  0.0  0.0  0.0
246  2566010.0  2566013.0  2566011.0  2566014.0 ...   0.0  0.0  0.0  0.0
247  2540614.0  2540612.0  2555357.0  2540610.0 ...   0.0  0.0  0.0  0.0
248  2722985.0  2722982.0  2722983.0  2722984.0 ...   0.0  0.0  0.0  0.0
249  2511111.0  2511113.0  2511114.0  2511115.0 ...   0.0  0.0  0.0  0.0
250  2552243.0  2552251.0  2552252.0  2556968.0 ...   0.0  0.0  0.0  0.0
251  2719909.0  2719912.0  2719915.0  2722993.0 ...   0.0  0.0  0.0  0.0
252  2694249.0  2694259.0  2694260.0  2694258.0 ...   0.0  0.0  0.0  0.0
253  2723087.0  2723089.0  2723080.0  2723079.0 ...   0.0  0.0  0.0  0.0
254  2694521.0  2694524.0  2694525.0  2694526.0 ...   0.0  0.0  0.0  0.0
255  2216784.0  2207483.0  2215115.0  2172705.0 ...   0.0  0.0  0.0  0.0

[256 rows x 33 columns]
>>> items[items!=0]=1
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    items[items!=0]=1
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 3114, in __setitem__
    self._setitem_frame(key, value)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 3161, in _setitem_frame
    self._check_inplace_setting(value)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\generic.py", line 4503, in _check_inplace_setting
    raise TypeError('Cannot do inplace boolean setting on '
TypeError: Cannot do inplace boolean setting on mixed-types with a non np.nan value
>>> items
		    
       ItemGroupId       I1         I2         I3 ...   I31  I32  I33  I34
0    1_13069000301  2274736        0.0        0.0 ...   0.0  0.0  0.0  0.0
1    1_13069000502  2556261  2556259.0  2556257.0 ...   0.0  0.0  0.0  0.0
2    1_13069000701  2458678  2274748.0        0.0 ...   0.0  0.0  0.0  0.0
3    1_13069060001  2274773        0.0        0.0 ...   0.0  0.0  0.0  0.0
4    1_13602713301  2366859  2274795.0        0.0 ...   0.0  0.0  0.0  0.0
5    1_15326560001  2479975        0.0        0.0 ...   0.0  0.0  0.0  0.0
6    1_30235000101  2274876  2274878.0  2274877.0 ...   0.0  0.0  0.0  0.0
7    1_30796060201  2617789  2617788.0  2617787.0 ...   0.0  0.0  0.0  0.0
8    1_30831700301  2275443  2275445.0  2275437.0 ...   0.0  0.0  0.0  0.0
9    1_30849911701  2275607  2275604.0  2275610.0 ...   0.0  0.0  0.0  0.0
10   1_31081110001  2275906  2348465.0  2275908.0 ...   0.0  0.0  0.0  0.0
11   1_31242200301  2479982  2479983.0  2479984.0 ...   0.0  0.0  0.0  0.0
12   1_31242200601  2512435  2512431.0  2512430.0 ...   0.0  0.0  0.0  0.0
13   1_31249813401  2368523        0.0        0.0 ...   0.0  0.0  0.0  0.0
14   1_31283400401  2539179  2481204.0  2493149.0 ...   0.0  0.0  0.0  0.0
15   1_31741501301  2721989        0.0        0.0 ...   0.0  0.0  0.0  0.0
16   1_31775403901  2643764  2643759.0  2643765.0 ...   0.0  0.0  0.0  0.0
17   1_31842903201  2276763  2276752.0  2276764.0 ...   0.0  0.0  0.0  0.0
18   1_31842904101  2361482        0.0        0.0 ...   0.0  0.0  0.0  0.0
19   1_31842930501  2276935  2276934.0  2276936.0 ...   0.0  0.0  0.0  0.0
20   1_32521320501  2720062  2724163.0  2724164.0 ...   0.0  0.0  0.0  0.0
21   1_32521350701  2277194  2277193.0        0.0 ...   0.0  0.0  0.0  0.0
22   1_33214802401  2469337        0.0        0.0 ...   0.0  0.0  0.0  0.0
23   1_33214810601  2277326  2277329.0  2277328.0 ...   0.0  0.0  0.0  0.0
24   1_33214811601  2469338        0.0        0.0 ...   0.0  0.0  0.0  0.0
25   1_33214860801  2277359  2277358.0  2277361.0 ...   0.0  0.0  0.0  0.0
26   1_33255080001  2277582  2277571.0  2277573.0 ...   0.0  0.0  0.0  0.0
27   1_35515210601  2277854        0.0        0.0 ...   0.0  0.0  0.0  0.0
28   1_36088400101  2416984  2416983.0  2416982.0 ...   0.0  0.0  0.0  0.0
29   1_37781212301  2721993        0.0        0.0 ...   0.0  0.0  0.0  0.0
..             ...      ...        ...        ... ...   ...  ...  ...  ...
226  1_91777680101  2398962  2398963.0  2368213.0 ...   0.0  0.0  0.0  0.0
227  1_91779600201  2428134  2428135.0  2428137.0 ...   0.0  0.0  0.0  0.0
228  1_91820620001  2368280  2368284.0  2368286.0 ...   0.0  0.0  0.0  0.0
229  1_91820660001  2428156  2428153.0  2428155.0 ...   0.0  0.0  0.0  0.0
230  1_91820660101  2556720  2556721.0  2556722.0 ...   0.0  0.0  0.0  0.0
231  1_91820700301  2407744  2376189.0  2376192.0 ...   0.0  0.0  0.0  0.0
232  1_91823000301  2362553  2362551.0  2362563.0 ...   0.0  0.0  0.0  0.0
233  1_91823010001  2366676  2366668.0  2366669.0 ...   0.0  0.0  0.0  0.0
234  1_91826400301  2450328  2450327.0  2450322.0 ...   0.0  0.0  0.0  0.0
235  1_91835840001  2421999  2421995.0  2421990.0 ...   0.0  0.0  0.0  0.0
236  1_91971500201  2535866  2535863.0  2535867.0 ...   0.0  0.0  0.0  0.0
237  1_92149040701  2701504  2692249.0  2701502.0 ...   0.0  0.0  0.0  0.0
238  1_92149240001  2382198  2382199.0  2382196.0 ...   0.0  0.0  0.0  0.0
239  1_92151440701  2721271  2726639.0  2724337.0 ...   0.0  0.0  0.0  0.0
240  1_92206510401  2387078        0.0        0.0 ...   0.0  0.0  0.0  0.0
241  1_92293340001  2347308  2347304.0  2347303.0 ...   0.0  0.0  0.0  0.0
242  1_92362000701  2347736  2347735.0  2347737.0 ...   0.0  0.0  0.0  0.0
243  1_94206000101  2357672  2357671.0  2407855.0 ...   0.0  0.0  0.0  0.0
244  1_94380640101  2735684  2735683.0  2735686.0 ...   0.0  0.0  0.0  0.0
245  1_AA051200201  2561585  2561583.0  2561586.0 ...   0.0  0.0  0.0  0.0
246  1_AA110900501  2566008  2566010.0  2566013.0 ...   0.0  0.0  0.0  0.0
247  1_AA134772501  2540613  2540614.0  2540612.0 ...   0.0  0.0  0.0  0.0
248  1_AA249410601  2726673  2722985.0  2722982.0 ...   0.0  0.0  0.0  0.0
249  1_AA396600301  2511116  2511111.0  2511113.0 ...   0.0  0.0  0.0  0.0
250  1_AA430201101  2552250  2552243.0  2552251.0 ...   0.0  0.0  0.0  0.0
251  1_AH678800101  2719910  2719909.0  2719912.0 ...   0.0  0.0  0.0  0.0
252  1_AJ202400101  2694263  2694249.0  2694259.0 ...   0.0  0.0  0.0  0.0
253  1_AJ516590101  2723086  2723087.0  2723089.0 ...   0.0  0.0  0.0  0.0
254  1_AJ731601001  2694522  2694521.0  2694524.0 ...   0.0  0.0  0.0  0.0
255  1_DUMMY0SKU01  2216783  2216784.0  2207483.0 ...   0.0  0.0  0.0  0.0

[256 rows x 35 columns]
>>> items[items.loc[:,'I2':'I34']!=0]=1
		    
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    items[items.loc[:,'I2':'I34']!=0]=1
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 3114, in __setitem__
    self._setitem_frame(key, value)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 3161, in _setitem_frame
    self._check_inplace_setting(value)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\generic.py", line 4503, in _check_inplace_setting
    raise TypeError('Cannot do inplace boolean setting on '
TypeError: Cannot do inplace boolean setting on mixed-types with a non np.nan value
>>> 
		    
>>> 
		    
>>> import numpy as np
		    
>>> 
		    
>>> 
		    
>>> 
		    
>>> type(items)
		    
<class 'pandas.core.frame.DataFrame'>
>>> 
		    
>>> items[items.loc[:,'I2':'I34']!=0]=1
		    
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    items[items.loc[:,'I2':'I34']!=0]=1
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 3114, in __setitem__
    self._setitem_frame(key, value)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 3161, in _setitem_frame
    self._check_inplace_setting(value)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\generic.py", line 4503, in _check_inplace_setting
    raise TypeError('Cannot do inplace boolean setting on '
TypeError: Cannot do inplace boolean setting on mixed-types with a non np.nan value
>>> items[items.loc[1:,'I2':'I34']!=0]=1
		    
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    items[items.loc[1:,'I2':'I34']!=0]=1
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 3114, in __setitem__
    self._setitem_frame(key, value)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 3161, in _setitem_frame
    self._check_inplace_setting(value)
  File "C:\Users\nabhinav\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\generic.py", line 4503, in _check_inplace_setting
    raise TypeError('Cannot do inplace boolean setting on '
TypeError: Cannot do inplace boolean setting on mixed-types with a non np.nan value
>>> 
		    
>>> 
		    







      

      
