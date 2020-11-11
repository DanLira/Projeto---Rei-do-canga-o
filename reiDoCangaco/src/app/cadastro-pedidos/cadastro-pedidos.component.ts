import { Component, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';

@Component({
  selector: 'app-pedidos',
  templateUrl: './cadastro-pedidos.component.html',
  styleUrls: ['./cadastro-pedidos.component.scss']
})
export class CadastroPedidosComponent implements OnInit {

  formsRegister: FormGroup;
  constructor() { }

  ngOnInit() {
  }

}
