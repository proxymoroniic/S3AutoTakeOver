# S3 AutoTakeOver
This consists of two scripts to automate subdomain takeover.
## Installation



```bash
git clone https://github.com/subzero-sh/S3AutoTakeOver.git
cd S3AutoTakeOver
pip3 install -r requirements.txt
```

## Usage
**take.py**


Fill out your credentials of AWS in auth.cfg to use take.py. 
Take is an automation script for subdomain takeover which has a CNAME with a bucket,but the original bucket might have been deleted by the owner. This detects a whether it is vulnerable to a subdomain takeover and creates a aws S3 bucket with the same bucket name, hence the domain points to your subdomain and resulting in a subdomain takeover.  

```python
python take.py <subdomain>
```

**buckettake.py**

This is an automation script to check wheather bucket is avaliable for takeover or not.

```python
python buckettake.py -u <valid bucket>
```
