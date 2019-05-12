import {Component, OnInit} from '@angular/core';
import {ProviderService} from '../../../shared/service/provider.service';
import {Item} from '../../../shared/model/model';
import {ActivatedRoute, Router} from '@angular/router';

@Component({
  selector: 'app-items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.scss']
})
export class ItemsComponent implements OnInit {

  private items: Item[];

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private provider: ProviderService
  ) { }

  ngOnInit() {
    this.items = [
      {
        title: 'Glasses',
        description: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. ' +
          'Accusantium aperiam aut culpa cum dignissimos ea eius eum facere fuga neque nihil, ' +
          'nulla omnis quasi quia reiciendis sed sit, voluptate voluptatibus!',
        category: 'Accessoires',
        owner: 'zhanel',
        post_date: new Date(),
        price: 250,
        like_count: 17
      }
    ];
    this.items.push(this.items[0]);
  }

  onItemClick(item: Item) {
  }

  onPostItemClick() {
    this.router.navigateByUrl('/post-item');
  }
}
