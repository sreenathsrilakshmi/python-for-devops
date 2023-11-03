#code to slice a list
#list the s3 buckets
s3_buckets_list=["abhishek_demo_bucket","Srilakshmi_demo_bucket","Shruti_S3_Demo_bucket", "Sreenath_demo_bucket","Sinduri_S3_Demo_bucket"]
new_list= s3_buckets_list[0:3] ## code always prints upper bound-1 (3-1=2) 0,1,2 elements are printed as the output 
print(s3_buckets_list[0])
