import {Component, OnInit} from '@angular/core';
import {ProviderService} from '../../../shared/service/provider.service';

@Component({
  selector: 'app-items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.scss']
})
export class ItemsComponent implements OnInit {

  constructor(private provider: ProviderService) {
  }

  ngOnInit() {
  }

}
