#!/bin/bash
doc_path=docs/
sidebar_path=$doc_path"_sidebar.md"

function deal_file(){
    # 将空格替换为%20（html空格）
    for element in `ls -1 $1 | sed "s/[ ]/%20/g"`
    do
        dir_or_file=$1"/"$element
        counter=`echo $dir_or_file | grep -o / | wc -l`
        let counter-=2
        if [ -d $dir_or_file ] ;
        then
            if [ "$element" != "assets" ];then
                printf '%0.s  ' $(seq 0 $counter) >> $sidebar_path
                echo "- $element" >> $sidebar_path
                deal_file $dir_or_file
            fi
        else
            printf '%0.s  ' $(seq 0 $counter) >> $sidebar_path
            path=`echo $dir_or_file`
            # 去掉前面的docs/，只取相对路径
            relative_path=`echo ${path/$doc_path/}`
            title=`echo $element | sed "s/.md//" | sed "s/%20/ /g"`
            echo "- [$title]($relative_path)" >> $sidebar_path
        fi
    done
}

root_dir=`ls -d docs/*/`

:> $sidebar_path
echo "- [README](README.md)" >> $sidebar_path
for dir in $root_dir
do
    if [ "$dir" = "." ]
    then
        continue
    else
        C1=`echo $dir | cut -f2 -d '/'`
        echo "- $C1" | cut -f2 -d '/' >> $sidebar_path
        # 去掉最后一个字符/
        deal_file `echo $dir | sed 's/.$//'`
    fi
done