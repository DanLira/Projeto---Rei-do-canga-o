export interface Produto {
    _id?: string;
    nome: string;
    descricao: string;
    precoVenda: number;
    precoCusto: number;
    categoria: string;
    quantidade: number;
    createdAt?: Date;
    updatedAt?: Date;

}