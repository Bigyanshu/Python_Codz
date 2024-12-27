# Match stmt is similar with Switch stmt
def http_status(status) :
    match_status:(status)    
    case200:(status) 
    return "200 OK"
    case404:(status) 
    return "404 is Not Found"
    case500:(status)
    return "500 Internal Server Error"
    case_:(status) 
    return "Unknown Status Code"