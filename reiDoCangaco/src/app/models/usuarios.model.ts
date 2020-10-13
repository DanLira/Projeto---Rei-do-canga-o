export interface Usuarios {
    _id?: string;
    nome: string;
    email: string;
    login: string;
    senha: string;
    createdAt?: Date;
    updatedAt?: Date;
    ativo?: boolean;
}
