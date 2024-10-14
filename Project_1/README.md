Using a real-world example, I will utilize CloudTrail to capture AWS events. I will set a rule in EventBridge to trigger a Lambda function whenever a user creates a new AWS EC2 instance. Then I use Python within that Lambda to tag that instance with the name of the user that created it.

![1](https://github.com/user-attachments/assets/9363be85-d706-481d-99ce-e15d9308d03d)
