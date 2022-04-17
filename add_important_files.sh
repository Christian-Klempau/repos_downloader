HOWTO="Usage: $0 -o <path/to/activity/repo> file1, file2, ..."

HELP="Copia los archivos file1, file2, ... en la base de los repos de todos los alumnos de una actividad. Se debe pasar el path a la carpeta de la actividad y el path a cada uno de los archivos que se debe copiar.\n\n$HOWTO"

while getopts "o:h" optname; do
    case $optname in
        h) echo $HELP && exit 0;;
        o) o=$OPTARG;;
        ?) echo $HOWTO && exit 1;;   
    esac
done

if [ -z "$o" ]; then
    echo $HOWTO && exit 1;
fi

echo $o

shift $((OPTIND-1))

for file; do
    for dir in $o/*/; do
        cp $file $dir;
        echo "Copied $file to $dir"
    done
done
