# $1 - host folder for result
# $2 - container folder for result
# $3 - source site for processing
# $4 - is Debug mode?

docker build -t downloader:v1 ./image

# e.g: -v //d/tmp/:/tmp
docker run --rm -v $1:$2 -e SITE=$3 -e DEST=$2 -e DEBUG=$4 downloader:v1

### docker run --rm -v $1:$2 downloader:v1 --site=$3 --dest=$2 --debug=$4
