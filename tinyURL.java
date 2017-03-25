class TinyURL {
	int shorturltoId(String shortURL){
		int id = 0;
		for(int i = 0 ; i < shortURL.length() ; ++i){
			id = id * 62 + toBase62(shortURL.charAt(i));
		}
		return id;
	}	

	String idToShortURL(int id){
		String chars = "0123456789abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
		String short_url = "";
		while(id > 0){
			short_url = chars.charAt(id % 62) + short_url;
			id = id / 62;
		}
		while(short_url.length() < 6){
			short_url  = "0" + short_url;
		}
		return short_url;
	}	
	int toBase62(char c){
		String chars = "0123456789abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
		return chars.indexOf(c) > -1 ? chars.indexOf(c) : null;
	}
}
