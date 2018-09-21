
build:
	zip -r -j ./build/echelon-anki_v21.zip echelon

clean:
	rm -rf ./build/*

test: testclean
	cp -r ./echelon ~/.local/share/Anki2/addons21/echelon-test
	anki

testclean:
	rm -rf ~/.local/share/Anki2/addons21/echelon-test
