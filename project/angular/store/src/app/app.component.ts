import {Component, OnInit} from '@angular/core';
import {AuthService} from './shared/service/auth.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'store';

  constructor(
    private auth: AuthService,
    private router: Router) {
  }

  ngOnInit(): void {
  }

  onPostItemClick() {
    this.router.navigate(['/post-item']);
  }

  logout() {
    this.auth.logout();
  }

  onLoginClick() {
    this.router.navigate(['/login']);
  }

  isAuthenticated() {
    return this.auth.authenticated();
  }

  homeClick() {
    this.router.navigate(['/']);
  }
}
