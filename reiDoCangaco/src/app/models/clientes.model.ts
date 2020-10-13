import { Endereco } from './endereco.model';

export interface Clientes {
    _id?: string;
    nome: string;
    sexo: string;
    email: string;
    fone: string;
    endereco: Endereco [];
    ativo?: boolean;
}
