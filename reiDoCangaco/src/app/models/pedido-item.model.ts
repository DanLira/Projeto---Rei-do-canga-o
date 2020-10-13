import { Produto } from './produto.model';
import { Pedidos } from './pedidos.model';
export interface PedidoItem {
    _id?: string;
    pedido: Pedidos;
    produto: Produto[];
    valorItem: number;
    quantidadeItem: number;
}
