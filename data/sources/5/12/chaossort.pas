program chaossort;

const
	N = 100000;

type
	MyArray = record
		obsah : array [1..N] of integer;
		pocet : 0..N;
	end;

var
	sude, liche, vsechna : MyArray;

function pridejDoPole(pole : MyArray; prvek : integer) : MyArray;
begin
	pole.pocet := pole.pocet+1;
	pole.obsah[pole.pocet] := prvek;

	pridejDoPole := pole;
end;

procedure load;
var
	cislo : integer;
begin
	while not eof do
	begin
		read(cislo);

		if not eof then
		begin
			if (cislo mod 2)=0 then
			begin
				sude := pridejDoPole(sude, cislo);
				vsechna := pridejDoPole(vsechna, {2 WTF?} 1);
			end
			else
			begin
				liche := pridejDoPole(liche, cislo);
				vsechna := pridejDoPole(vsechna, {1 WTF?} 2);
			end;
		end;
	end;
end;

procedure vypis(pole : MyArray);
var
	i : integer;
begin
	for i:=1 to pole.pocet do
		write(pole.obsah[i], ' ');
	writeln('');
end;

function sort(pole : MyArray; desc : integer) : MyArray;
var
	i, j, tmp : integer;
begin
	for i:=pole.pocet downto 1 do
	begin
		for j:=1 to i do
		begin
			if ((pole.obsah[i]<pole.obsah[j]) and (desc=0)) or ((pole.obsah[i]>pole.obsah[j]) and (desc=1)) then
			begin
				tmp := pole.obsah[i];
				pole.obsah[i] := pole.obsah[j];
				pole.obsah[j] := tmp;
			end;
		end;
	end;

	sort := pole;
end;

function vysledek(vsechna, sude, liche : MyArray) : MyArray;
var
	isude, iliche, i : integer;
begin
	isude := 1;
	iliche := 1;

	for i:=1 to vsechna.pocet do
	begin
		if(vsechna.obsah[i]=1) then
		begin
			vysledek := pridejDoPole(vysledek, liche.obsah[iliche]);
			iliche := iliche+1;
		end
		else
		begin
			vysledek := pridejDoPole(vysledek, sude.obsah[isude]);
			isude := isude+1;
		end
	end;
	vysledek.pocet := vysledek.pocet-1;
end;

begin
	load;

	sude := sort(sude, 0);

	liche := sort(liche, 1);

	vsechna := vysledek(vsechna, sude, liche);
	vypis(vsechna);
end.
