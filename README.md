# BGItest
这是一条新员工转正考核题目解答
# 程序考核题
+ 拆分带有barcode标记的DNA序列（fasta格式），去除拆分后每个样本的冗余序列，并绘制去冗余序列后的GC content分布图。
具体要求：
 * 拆分样本。已有fasta序列文件**reads_of_insert.fa**，其含有两个样本的序列。barcode（16个base）信息位于每条序列的开头或结尾。要求根据barcode将reads_of_insert.fasta中的两个样本序列**拆分**出来，存放在相应的文件中，结果文件命名sample1.fa、sample2.fa。
 * 去冗余序列。将第1步得到的两个结果文件中的冗余序列（长度、碱基顺序完全一致）去除（即冗余序列只保留一条），生成去冗余后的文件，ID**行加入冗余数目信息**，并将序列按照冗余数目**倒序排列**，结果文件命名sample1.uniq.fa、sample2.uniq.fa。
 
+ 注：
 *    reads_of_insert.fa 见目录
 *    barcode 信息
      * ``` sample1 ```       
         **GTACACGCTGTGACTA**
      * ``` sample2 ```       
     ** TCTATGTCTCAGTAGT **
        
 * 待拆分序列的barcode，既可能位于待拆分序列开头、也可能位于待拆分序列结尾；即可能是提供的barcode序列，也可能是提供的barcode的反向互补序列。
 * 拆分容错： 在barcode 16个碱基的比较中，至多允许一个碱基错配。
