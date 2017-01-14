def wsgi(environ, start_response):
    qs=rnviron['QUERY_STRING']
    rsp=""
    for s in qs: rsp+=s+'\n'
    status = '200 OK'
    headers = [
('Content-Type', 'text/plain')
]
    start_response(status, headers )
    return [ rsp ]
    
