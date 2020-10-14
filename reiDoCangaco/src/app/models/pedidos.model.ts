import { Clientes } from './clientes.model';
import { Endereco } from './endereco.model';

export interface Pedidos {
    _id?: string;
    cliente: Clientes[];
    enderecoEntrega: Endereco[];
    valorPedido: number;
    valorTaxa: number;
    dataPedido: Date;
    status: string;
}
