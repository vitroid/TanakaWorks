sync:
	rsync -av --include="*/" --include="fort.1[0-9][0-9][0-9]" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270fbn/1 .
	rsync -av --include="*/" --include="temp.d" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270fbn/1 .

	rsync -av --include="*/" --include="fort.1[0-9][0-9][0-9]" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270fbn/3 .
	rsync -av --include="*/" --include="temp.d" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270fbn/3 .

	rsync -av --include="*/" --include="fort.1[0-9][0-9][0-9]" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270sbn/1/ L/
	rsync -av --include="*/" --include="temp.d" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270sbn/1/ L/

	rsync -av --include="*/" --include="fort.1[0-9][0-9][0-9]" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270fbm/0/ L1/
	rsync -av --include="*/" --include="temp.d" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270fbm/0/ L1/

	rsync -av --include="*/" --include="fort.1[0-9][0-9][0-9]" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270sbm/0/ S1/
	rsync -av --include="*/" --include="temp.d" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270sbm/0/ S1/

	rsync -av --include="*/" --include="fort.1[0-9][0-9][0-9]" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270fbl/0/ fbl/
	rsync -av --include="*/" --include="temp.d" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270fbl/0/ fbl/

	rsync -av --include="*/" --include="fort.1[0-9][0-9][0-9]" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270sbl/00/ sbl/
	rsync -av --include="*/" --include="temp.d" --exclude="*" 172.23.78.18:/u/tanaka/r7/co2/nmaco2/mdnev/t270sbl/00/ sbl/

%.mp4: %.mpg
	ffmpeg -i $< -pix_fmt yuv420p -vf scale=1440:-1 $@

%.2000.mp4: %.mpg
	ffmpeg -i $< -pix_fmt yuv420p -vf scale=2000:-1 $@

clean:
	-rm *.ppm # for VMD temp images

distclean:
	-rm *.mp4 *.mpg 