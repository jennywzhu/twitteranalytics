from searchtweets import ResultStream, gen_rule_payload, load_credentials
from searchtweets import collect_results

premium_search_args = load_credentials("~/.twitter_keys.yaml",
                                       yaml_key="search_tweets_premium",
                                       env_overwrite=False)

rule = gen_rule_payload("beyonce", results_per_call=100) # testing with a sandbox account
print(rule)

tweets = collect_results(rule,
                         max_results=100,
                         result_stream_args=premium_search_args) # change this if you need to

for tweet in tweets[0:10]: 
	print(tweet.all_text, '\n\n')

rs = ResultStream(rule_payload=rule,
                  max_results=500,
                  max_pages=1,
                  **premium_search_args)

print(rs)

tweets = list(rs.stream())

# using unidecode to prevent emoji/accents printing
for tweet in tweets[0:10]: 
	print(tweet.all_text, '\n\n')