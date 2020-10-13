import { Clientes } from './clientes.model';
import { Estabelecimento } from './estabelecimento.model';
import { Endereco } from './endereco.model';

export interface Pedidos {
    _id?: string;
    estabelecimento: Estabelecimento[];
    cliente: Clientes[];
    enderecoEntrega: Endereco[];
    valorPedido: number;
    valorTaxa: number;
    dataPedido: Date;
    status: string;
}
