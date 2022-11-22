from Repositorios.ResultadoRepositorio import ResultadoRepositorio
from Repositorios.MesaRepositorio import MesaRepositorio
from Repositorios.CandidatoRepositorio import CandidatoRepositorio

from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa 
from Modelos.Candidato import Candidato

class ResultadoControlador():
    def __init__(self):
        self.repositorioResultado = ResultadoRepositorio()
        self.repositorioCandidato = CandidatoRepositorio()
        self.repositorioMesa = MesaRepositorio()
    
    def index(self):
        return self.repositorioResultado.findAll()
    
    def create(self, infoResultado, id_mesa, id_candidato):
        nuevoResultado = Resultado(infoResultado)
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa = laMesa
        nuevoResultado.candidato = elCandidato
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    def update(self, id, infoResultado, id_mesa, id_candidato):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.repositorioResultado.save(elResultado)
    
    def delete(self, id):
        return self.repositorioResultado.delete(id)


    
    def getListarCandidatosMesa(self, id_mesa):
        return self.repositorioResultado.getListadoCandidatosInscritiosMesa(id_mesa)
        

    def getListarMesasDeInscritoCandidato(self, id_candidato):
        return self.repositorioResultado.getListadoMesasCandidatoInscrito(id_candidato)

    def getMayorVoto(self):
        return self.repositorioResultado.getNumeroVotacionMayorCandidato()
