user: lambdauser
pw: lambda@123
AccessKey ID: AKIAVCYHVJPW5TYCME7C
Secret Access Key: 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 


aws s3 mb s3://lambdademobucketlz

sam deploy --s3-bucket lambdademobucketlz --stack-name HelloWorldLambdaJava --capabilities CAPABILITY_IAM

