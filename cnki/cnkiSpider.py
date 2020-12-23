from urllib import request

url = "https://kns.cnki.net/KNS8/Brief/GetGridTableHtml"


head = {
    "Accept": "text/html, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Length": 888,
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": 'Ecp_ClientId=5191215094400636506; RsPerPage=20; cnkiUserKey=579c3ab3-5507-6cf1-2acc-29e1697ef41d; LID=WEEvREcwSlJHSldSdmVqM1BLUWh5QjR6Zk1NS0tLbG83YWhpNzYvZEJwQT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; Ecp_session=1; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"nj0236","ShowName":"%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6","UserType":"bk","BUserName":"","BShowName":"","BUserType":"","r":"dWRuQ0"}; ASP.NET_SessionId=1p4ncl4ggmvajetdmwidspbf; SID_kns8=123122; _pk_ref=%5B%22%22%2C%22%22%2C1606790032%2C%22https%3A%2F%2Fcnki.net%2F%22%5D; _pk_ses=*; CurrSortField=%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2f(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27TIME%27); CurrSortFieldType=desc; Ecp_ClientIp=114.214.225.57; SID_kns_new=kns123115; c_m_LinID=LinID=WEEvREcwSlJHSldSdmVqM1BLUWh5QjR6Zk1NS0tLbG83YWhpNzYvZEJwQT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=12/01/2020 10:52:31; c_m_expire=2020-12-01 10:52:31',
    "Host": 'kns.cnki.net',
    "Origin": "https://kns.cnki.net",
    "Referer": "https://kns.cnki.net/kns8/defaultresult/index",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47",
    "X-Requested-With": "XMLHttpRequest"
}