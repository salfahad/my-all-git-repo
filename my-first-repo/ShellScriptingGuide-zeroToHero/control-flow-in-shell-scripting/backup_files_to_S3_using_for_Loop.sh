##Practical Examples Using Control Flow

##Example: Backup Files to S3 Using a for Loop

#!/bin/bash
##With and without --recursive
<<comment
DIRECTORY="/home/ec2-user/my-project-repo/my-first-repo/ShellScriptingGuide-zeroToHero/control-flow-in-shell-scripting"
BUCKET_NAME="my-new-bucket-fullofpotato"
if [ -d "$DIRECTORY" ]; then
    for FILE in $DIRECTORY/*; do
        aws s3 cp $FILE s3://$BUCKET_NAME/ --recursive

        echo "Uploaded $FILE to $BUCKET_NAME" 
    done
else
    echo "Directory $DIRECTORY does not exist."
fi
comment

DIRECTORY="/home/ec2-user/my-project-repo/my-first-repo/ShellScriptingGuide-zeroToHero/control-flow-in-shell-scripting"
BUCKET_NAME="my-new-bucket-fullofpotato"
if [ -d "$DIRECTORY" ]; then
    for FILE in $DIRECTORY/*; do
        aws s3 cp $FILE s3://$BUCKET_NAME/

        echo "Uploaded $FILE to $BUCKET_NAME" 
    done
else
    echo "Directory $DIRECTORY does not exist."
fi