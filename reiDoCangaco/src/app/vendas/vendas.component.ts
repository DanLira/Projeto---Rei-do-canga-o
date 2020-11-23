import { PedidoProduto } from './../models/pedido-produto.model';
import { Component, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { MatDialog, MatPaginator, MatSort, MatTableDataSource } from '@angular/material';
import { PedidoService } from '../cadastro-pedidos/pedidoService.service';
import { Pedidos } from '../models/pedidos.model';
import { ModalDetalhesVendaComponent } from '../shared/component/modals/modalDetalhesVenda/modalDetalhesVenda.component';

@Component({
  selector: 'app-vendas',
  templateUrl: './vendas.component.html',
  styleUrls: ['./vendas.component.scss']
})
export class VendasComponent implements OnInit {
  filterFormProduto: FormGroup;
  pedidoList: Pedidos [];
  displayedColumns: string[] = ['codigo', 'valorTotal', 'dataPedido', 'detalhe'];
  dataSource = new MatTableDataSource<Pedidos>();
  @ViewChild('MatPaginator') MatPaginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(private readonly formBuilder: FormBuilder,
              public dialog: MatDialog,
              private readonly pedidoService: PedidoService) { }

  ngOnInit() {
    this.dataSource.sort = this.sort;
    this.filterFormProduto = this.formBuilder.group({
      descricaoFilterCtrl: ['']
    });

    this.pedidoService.getAllPedido().subscribe((pedido: Pedidos[]) => {
      this.pedidoList = (!!pedido) ? pedido : [];
      this.dataSource.data = [...this.pedidoList];
    });

    this.dataSource.paginator = this.MatPaginator;
  }


  filterTabelaPedido(): void {
    let filteredTable: Pedidos[] = this.pedidoList;
    if (!this.filterFormProduto.value.descricaoFilterCtrl) {
      this.dataSource.data = [...this.pedidoList];
    }
    if (this.filterFormProduto.value.descricaoFilterCtrl) {
      filteredTable = filteredTable.filter
      ( x => {
        return x.descProduto ? x.descProduto.toUpperCase().includes(this.filterFormProduto.value.descricaoFilterCtrl.toUpperCase()) : null;
      });
     }
    this.dataSource.data = filteredTable;
  }

  openVendasDetalhes(value: Pedidos): void {
    this.dialog.open(ModalDetalhesVendaComponent, {
      data: {
        detalhes: value
      }
    });
  }

}
