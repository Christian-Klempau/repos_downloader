HOWTO="Usage: $0 -a <actividad> -p <path/to/csv> -c <corrector>"


while getopts "a:c:p:" optname; do
    case $optname in
        a) a=$OPTARG;;
        c) c=$OPTARG;;
        p) p=$OPTARG;;
        ?) echo $HOWTO && exit 1;;   
    esac
done

if [ -z "$a" ] || [ -z "$c" ] || [ -z "$p" ]; then
    echo $HOWTO && exit 1;
fi

path_repo="git@github.com:IIC2233/${a}.git"

mkdir $a

cd $a

git init

git sparse-checkout init

git remote add -f origin $path_repo

my_students=

INPUT="../$p"
OLDIFS=$IFS
IFS=','
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read student_github assistant_github commit_hash
do
    if [ $assistant_github = $c ]; then
        my_students="$my_students $student_github"
    fi
done < $INPUT
IFS=$OLDIFS

eval "git sparse-checkout set $my_students"
git pull origin master
