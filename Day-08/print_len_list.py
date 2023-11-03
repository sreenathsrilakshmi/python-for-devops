#lists add data to the existing list
#list the s3 buckets
s3_buckets_list=["abhishek_demo_s3_bucket","Srilakshmi_demo_s3_bucket","Shruti_S3_Demo_bucket","test_demo_s3_bucket","sreenath_demo_s3_bucket"]
print(len(s3_buckets_list))
s3_buckets_list.append("new_s3_bucket")
print(len(s3_buckets_list))
s3_buckets_list.remove("test_demo_s3_bucket")
s3_buckets_list.remove("abhishek_demo_s3_bucket")
print(len(s3_buckets_list))
