sync:
	rsync -av --include="*/" --include="fort.1[0-9][0-9][0-9]" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270fbn/1 .
	rsync -av --include="*/" --include="fort.1[0-9][0-9][0-9]" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270fbn/3 .
	rsync -av --include="*/" --include="fort.1[0-9][0-9][0-9]" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270sbn/1/ L/
	rsync -av --include="*/" --include="temp.d" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270fbn/1 .
	rsync -av --include="*/" --include="temp.d" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270fbn/3 .
	rsync -av --include="*/" --include="temp.d" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270sbn/1/ L/

clean:
	rm *.ppm # for VMD temp images