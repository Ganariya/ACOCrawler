from ACOCrawler.acocrawler import AcoCrawler

# the keyword you want to crawl
keyword = "competitive programming"

# the keywords related to keyword
keywords = [
    "competitive programming",
    "c++",
    "atcoder",
    "codeforces",
    "yukicoder"
]

# how many cycles you scrape
num_of_cycles = 100

# how many ants to scrape
num_of_ants = 10

# ant colony optimization parameters with max-min aco
alpha = 1
beta = 1
rho = 0.9
lower = 0.0001
upper = 1

# parameters to score the page
# how related to keyword
base_phe = 100
init_phe = 0.001

# the parameter score is larger than collect_norm, neo4j saves the page
# if score < collect_norm, this page doesn't include neo4j because this page doesn't relate to keyword.
collect_norm = 0.00001

# parameter
# init_node parameter
init_node_score = 0.1

crawler = AcoCrawler(keyword=keyword, num_of_cycles=num_of_cycles, num_of_ants=num_of_ants, keywords=keywords, alpha=alpha, beta=beta, rho=rho, lower=lower, upper=upper, base_phe=base_phe, init_phe=init_phe, collect_norm=collect_norm, init_node_score=init_node_score)

# start node makes
crawler.start()

# aco
crawler.solve()
crawler.finish()
