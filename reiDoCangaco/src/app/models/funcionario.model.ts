import { Usuarios } from './usuarios.model';

export interface Funcionario {
    _id?: string;
    usuario: Usuarios [];
    funcao: string;
}