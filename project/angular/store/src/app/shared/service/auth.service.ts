import { Injectable } from '@angular/core';
import {ProviderService} from './provider.service';
import {IAuthResponse} from '../model/model';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private provider: ProviderService
  ) { }

  public authenticated(): boolean {
    const item = localStorage.getItem('token');
    return typeof item !== 'undefined' && item != null;
  }

  authenticate(username: string, password: string): Promise<IAuthResponse> {
    return this.provider.login(username, password).then(res => {
      localStorage.setItem('token', res.token);
      return res;
    });
  }

  logout() {
    localStorage.clear();
    this.provider.logout();
  }
}
