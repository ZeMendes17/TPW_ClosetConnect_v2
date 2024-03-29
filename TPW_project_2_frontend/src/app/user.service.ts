import {Injectable} from '@angular/core';
import {User} from "./user";
import {Comment} from "./comment";

@Injectable({
  providedIn: 'root'
})

export class UserService {
  private baseUrl: string = "http://zemendes.pythonanywhere.com/ws/";

  constructor() { }

  async getUsers(): Promise<User[]> {
    const url: string = this.baseUrl + "users";
    const data: Response = await fetch(url);
    // the image is a base64 string
    // we need to convert it to a blob
    // and then to an url
    const users: User[] = await data.json() ?? [];
    for (let user of users) {
      const blob: Blob = base64toBlob(user.image, "image/jpg");
      user.image = URL.createObjectURL(blob);
    }
    return users;
  }

  async getUser(id: number): Promise<User> {
    const url: string = this.baseUrl + "user/" + id;
    const data: Response = await fetch(url);
    const user: User = await data.json() ?? null;
    if (user) {
      const blob: Blob = base64toBlob(user.image_base64, "image/jpg");
      user.image_base64 = URL.createObjectURL(blob);
    }
    return user;
  }


  async deleteUser(id: number): Promise<Response> {
    try {
      const url: string = this.baseUrl + "delete_user/" + id;
      const data: Response = await fetch(url, {
        method: "DELETE",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: id })
      });

      if (!data.ok) {
        throw new Error(data.statusText);
      }

      return data;
    } catch (error) {
      console.error("Error deleting user:", error);
      throw error;
    }
  }

  async getUserByUsername(username: string): Promise<User> {
    const url: string = this.baseUrl + "user/" + username;
    const data: Response = await fetch(url);
    const user: User = await data.json() ?? null;
    if (user) {
      const blob: Blob = base64toBlob(user.image_base64, "image/jpg");
      user.image_base64 = URL.createObjectURL(blob);
    }
    return user;
  }

  async getUserComments(id: number): Promise<Comment[]> {
    const url: string = this.baseUrl + "user/comments/" + id;
    const data: Response = await fetch(url);
    return await data.json() ?? [];
  }
}



// Function to convert a base64 string to a Blob
function base64toBlob(base64Data: string, contentType: string): Blob {
  const sliceSize = 512;
  const byteCharacters = atob(base64Data);
  const byteArrays: Uint8Array[] = [];

  for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
    const slice = byteCharacters.slice(offset, offset + sliceSize);
    const byteNumbers = new Array(slice.length);
    for (let i = 0; i < slice.length; i++) {
      byteNumbers[i] = slice.charCodeAt(i);
    }
    const byteArray = new Uint8Array(byteNumbers);
    byteArrays.push(byteArray);
  }

  return new Blob(byteArrays, { type: contentType });
}
