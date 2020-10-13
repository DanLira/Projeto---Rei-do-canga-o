import { Endereco } from './endereco.model';
export interface Estabelecimento {
    _id?: string;
    nome: string;
    endereco: Endereco[];
    fone: string;
    email?: string;
    cnpj: string;
    horarioAtendimento: string;
    aberto?: boolean;
}
