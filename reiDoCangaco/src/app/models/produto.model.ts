export interface Produto {
    _id?: string;
    descProduto: string;
    descAbrevProduto: string;
    preco: number;
    unidadeMedCompra: number;
    unidadeMedVenda: number;
    tipoVolume: number;
    fornecedorPj?: string;
    fornecedorPf?: string;
    createdAt?: Date;
    updatedAt?: Date;

}
