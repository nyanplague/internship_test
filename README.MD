Open the terminal inside the project and enter the following commands:

1) docker build . -t docker_python
2) docker run -d -p 5000:5000 docker_python

Use the app on your local host with 5000 port.

Without Limit:
http://localhost:5000/paraphrase?tree=(S%20(NP%20(NP%20(DT%20The)%20(JJ%20charming)%20(NNP%20Gothic)%20(NNP%20Quarter))%20(,%20,)%20(CC%20or)%20(NP%20(NNP%20Barri)%20(NNP%20G%C3%B2tic)))%20(,%20,)%20(VP%20(VBZ%20has)%20(NP%20(NP%20(JJ%20narrow)%20(JJ%20medieval)%20(NNS%20streets))%20(VP%20(VBN%20filled)%20(PP%20(IN%20with)%20(NP%20(NP%20(JJ%20trendy)%20(NNS%20bars))%20(,%20,)%20(NP%20(NNS%20clubs))%20(CC%20and)%20(NP%20(JJ%20Catalan)%20(NNS%20restaurants))))))))

With Limit 3:
http://localhost:5000/paraphrase?tree=(S%20(NP%20(NP%20(DT%20The)%20(JJ%20charming)%20(NNP%20Gothic)%20(NNP%20Quarter))%20(,%20,)%20(CC%20or)%20(NP%20(NNP%20Barri)%20(NNP%20G%C3%B2tic)))%20(,%20,)%20(VP%20(VBZ%20has)%20(NP%20(NP%20(JJ%20narrow)%20(JJ%20medieval)%20(NNS%20streets))%20(VP%20(VBN%20filled)%20(PP%20(IN%20with)%20(NP%20(NP%20(JJ%20trendy)%20(NNS%20bars))%20(,%20,)%20(NP%20(NNS%20clubs))%20(CC%20and)%20(NP%20(JJ%20Catalan)%20(NNS%20restaurants))))))))&limit=3
